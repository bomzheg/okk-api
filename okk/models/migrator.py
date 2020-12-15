from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

migrator = Migrate()


def init_migrator(app: Flask, db: SQLAlchemy):
    with app.app_context():
        if db.engine.url.drivername == 'sqlite':
            migrator.init_app(app, db, render_as_batch=True)
        else:
            migrator.init_app(app, db)
