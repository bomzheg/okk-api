from flask import Flask


def index():
    return "Привет"


def setup_hello(app: Flask):
    app.add_url_rule('/', 'index', index)
