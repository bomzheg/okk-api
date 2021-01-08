from flask import Flask

from okk.config import config, Config, WebConfig
from okk.middleware.acl import ACLMiddleware
from okk.routes import setup_all_routes
from okk.models import init_db, db, init_migrator


def create_web_server():
    flask_app = Flask(__name__)
    app = configure_web_server(flask_app, config)
    return app


def configure_web_server(app: Flask, current_config: Config):
    setup_all_routes(app, current_config)
    app.config.from_object(current_config.flask_config)
    app.wsgi_app = ACLMiddleware(app.wsgi_app, current_config.allowed_tokens)
    init_db(app)
    init_migrator(app, db)
    return app


def run_web_server(app: Flask, web_config: WebConfig):
    app.run(
        host=web_config.url,
        port=web_config.port,
    )


if __name__ == '__main__':
    current_app = create_web_server()
    run_web_server(current_app, config.web_config)
