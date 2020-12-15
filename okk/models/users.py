from secrets import token_urlsafe

from .db import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), index=True)
    token = db.Column(db.String(64), default=lambda: token_urlsafe(48))

    __tablename__ = "users"
