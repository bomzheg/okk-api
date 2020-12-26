from flask import jsonify
from werkzeug.http import HTTP_STATUS_CODES

from okk.responses.common import not_ok


def error_response(status_code, message=None):
    payload = {**not_ok, 'error': HTTP_STATUS_CODES.get(status_code, 'Unknown error')}
    if message:
        payload['message'] = message
    response = jsonify(payload)
    response.status_code = status_code
    return response


def bad_request(message: str):
    return error_response(400, message)


def forbidden(message: str):
    return error_response(403, message)
