import json
import typing

from flask import Request, Response

from okk.responses.errors import wrap_error_message


class ACLMiddleware:
    """
    Current middleware support simple check auth by token.
    tokens is configured at start application and can't be changed next
    """
    def __init__(self, app, allowed_tokens: typing.Iterable):
        self.app = app
        self.allowed_tokens = allowed_tokens

    def __call__(self, environ, start_response):
        request = Request(environ, shallow=True)
        auth = request.headers['Authorization']
        j = json.loads(auth) or {}
        if 'token' not in j:
            res = _make_response(401, 'body must contains json with key "token"')
            return res(environ, start_response)
        if j['token'] not in self.allowed_tokens:
            res = _make_response(403, 'token invalid')
            return res(environ, start_response)
        return self.app(environ, start_response)


def _make_response(status_code: int, message: str):
    return Response(
        json.dumps(wrap_error_message(status_code, message)),
        mimetype='application/json',
        status=status_code
    )
