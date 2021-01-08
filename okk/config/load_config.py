import os
from pathlib import Path

from dotenv import load_dotenv

from .config_type import DBConfig, Config, WebConfig, FlaskConfig, RZNLogin


app_dir = Path(__file__).parent.parent.parent
load_dotenv(str(app_dir / '.env'))

files_dir = app_dir / "files"

pg_config = DBConfig(
    db_type="postgres",
    host=os.getenv("DB_IP", default='192.168.1.39'),
    port=int(os.getenv("DB_PORT", default=5432)),
    login=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    db_name=os.getenv("DB_NAME", default='batchs'),
)

sqlite_config = DBConfig(
    db_type="sqlite",
    db_name=os.getenv("SQLITE_PATH", default=app_dir / "okk.db"),
)
DB_TYPE = os.getenv("DB_TYPE")
if DB_TYPE is None or DB_TYPE == "sqlite":
    current_db_config = sqlite_config
else:
    current_db_config = pg_config

web_config = WebConfig(
    url=os.getenv("WEB_URL", default="127.0.0.1"),
    port=os.getenv("WEB_PORT", default=5000),
)

flask_config = FlaskConfig(
    SQLALCHEMY_DATABASE_URI=current_db_config.connect_str,
    SQLALCHEMY_TRACK_MODIFICATIONS=False,
    JSONIFY_PRETTYPRINT_REGULAR=True,
    SECRET_KEY=os.getenv("SECRET_TOKEN", default="AgACAgIAAxk_7dfV98j2sSgU1d1Ej3CCc2nBAACe68xG18sQEq5"),
    UPLOAD_FOLDER=files_dir / "temp",
)

rzn_login = RZNLogin(
    login=os.getenv("LOGIN"),
    password=os.getenv("PASSWORD"),
)

config = Config(
    app_dir=app_dir,
    files_for_db_dir=files_dir,
    allowed_extensions=frozenset({".pdf"}),
    allowed_tokens=frozenset({os.getenv("TOKEN")}),
    db_config=current_db_config,
    web_config=web_config,
    flask_config=flask_config,
    rzn_login=rzn_login,
)
