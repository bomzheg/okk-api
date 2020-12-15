from flask import Flask

from okk.config.config_type import Config
from .hello import setup_hello
from .batch_info import setup_batch_info
from .file_upload import setup_upload_file


def setup_all_routes(app: Flask, config: Config):
    setup_hello(app)
    setup_batch_info(app, config.rzn_login)
    setup_upload_file(app, config.allowed_extensions, config.files_for_db_dir)
