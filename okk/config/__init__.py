from .config_type import Config, DBConfig, WebConfig, FlaskConfig
from .load_config import config, web_config

__all__ = [
    Config, DBConfig, WebConfig, FlaskConfig,
    config, web_config,
]
