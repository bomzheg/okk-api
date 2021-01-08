from flask import Flask

from okk.config import Config
from okk.middleware.acl import ACLMiddleware


def setup_middleware(app: Flask, current_config: Config):
    app.wsgi_app = ACLMiddleware(app.wsgi_app, current_config.allowed_tokens)
