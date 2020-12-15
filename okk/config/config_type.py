
from dataclasses import dataclass
from pathlib import Path


@dataclass
class DBConfig:
    db_type: str
    host: str = None
    port: int = None
    login: str = None
    password: str = None
    db_name: str = None

    @property
    def connect_str(self):
        if self.db_type == "sqlite":
            return f"{self.db_type}:///{self.db_name}"
        elif self.db_type in ("postgres", "mysql", "oracle"):
            return (
                f'{self.db_type}://{self.login}:{self.password}'
                f'@{self.host}:{self.port}/{self.db_name}'
            )
        else:
            raise ValueError("unsupported db type: ", self.db_type)


@dataclass
class WebConfig:
    url: str = None
    port: str = None
    debug: str = False


@dataclass
class FlaskConfig:
    SQLALCHEMY_DATABASE_URI: str = None
    SQLALCHEMY_TRACK_MODIFICATIONS: bool = None
    SECRET_KEY: str = None
    UPLOAD_FOLDER: Path = None


@dataclass
class RZNLogin:
    login: str
    password: str


@dataclass
class Config:
    app_dir: Path = None
    files_for_db_dir: Path = None
    allowed_extensions: frozenset = None
    db_config: DBConfig = None
    web_config: WebConfig = None
    flask_config: FlaskConfig = None
    rzn_login: RZNLogin = None




