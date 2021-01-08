from flask import jsonify
from werkzeug.http import HTTP_STATUS_CODES

from okk.responses.common import not_ok


def wrap_error_message(status_code: int, message: str):
    payload = {**not_ok, 'error': HTTP_STATUS_CODES.get(status_code, 'Unknown error')}
    if message:
        payload['message'] = message
    return payload


def error_response(status_code: int, message: str = None):
    payload = wrap_error_message(status_code, message)
    response = jsonify(payload)
    response.status_code = status_code
    return response


def bad_request(message: str):
    return error_response(400, message)


def forbidden(message: str):
    return error_response(403, message)


def unauthorized(message: str):
    return error_response(401, message)
