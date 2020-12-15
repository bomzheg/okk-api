from functools import partial

from flask import Flask, jsonify
from flask import request
from sqlalchemy.exc import IntegrityError

from okk.config.config_type import RZNLogin
from okk.models.db import db
from okk.routes.errors import bad_request, ok, forbidden
from okk.services.batchs import get_batch, patch_batch_service, prepare_batch_args, process_batch_creation
from okk.services.rzn_sender import RZNGaseous
from okk.services.send_gaseous_batch import send_batch


def get_batch_info(batch_id: int):
    batch = get_batch(batch_id)
    result_dict = ok
    result_dict['data'] = batch.to_dict()

    response = jsonify(result_dict)
    return response


def patch_batch(batch_id: int):
    data = request.get_json() or {}
    batch, patched = patch_batch_service(batch_id, data, db.session)
    if not patched:
        return bad_request("what you want to patch?")

    result_dict = ok
    result_dict['data'] = batch.to_dict()
    result_dict['patched'] = patched

    response = jsonify(result_dict)
    return response


def get_batchs():
    return forbidden("you cant not see all batchs")


def create_batch():
    data = request.get_json() or {}
    try:
        batch_kwargs = prepare_batch_args(data)
    except KeyError:
        return bad_request('request must include "seria" and "partia"')
    except ValueError:
        return bad_request("please use ISO 8601 for format date")

    try:
        batch = process_batch_creation(session=db.session, **batch_kwargs)
    except IntegrityError:
        return bad_request("that batch already exists")

    result_dict = ok
    result_dict['data'] = batch.to_dict()

    response = jsonify(result_dict)
    response.status_code = 201
    return response


def send_batch_route(batch_id: int, rzn_login: RZNLogin):
    batch = get_batch(batch_id)
    with RZNGaseous(rzn_login.login, rzn_login.password) as rzn_sender:
        send_batch(batch, rzn_sender)
    return jsonify(ok)


def setup_batch_info(app: Flask, rzn_login: RZNLogin):
    app.add_url_rule('/batchs/<int:batch_id>', 'GetBatchInfo', get_batch_info, methods=['GET'])
    app.add_url_rule('/batchs/<int:batch_id>', 'PatchBatchInfo', patch_batch, methods=['PATCH'])
    app.add_url_rule("/batchs", "AddNew", create_batch, methods=['POST'])
    app.add_url_rule("/batchs", "GetAllBatchs", get_batchs, methods=["GET"])
    app.add_url_rule(
        "/batchs/<int:batch_id>",
        "SendBatch",
        partial(send_batch_route, rzn_login=rzn_login),
        methods=['POST']
    )
