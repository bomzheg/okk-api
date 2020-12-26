from flask import Flask, jsonify

from okk.responses.common import ok


def index():
    result_dict = ok
    result_dict['data'] = "Hello"
    response = jsonify(result_dict)
    response.status_code = 200
    return response


def setup_hello(app: Flask):
    app.add_url_rule('/', 'index', index)
