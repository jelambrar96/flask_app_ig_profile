from enum import unique
from app import db


class Entry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64), index=True, nullable=False)
    description = db.Column(db.String(120), index=True, nullable=False)
    status = db.Column(db.Boolean, default=False)


class Profile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    profile = db.Column(db.String(64), index=True, nullable=False, unique=True)
    is_active = db.Column(db.Boolean, default=True)
    is_favorite = db.Column(db.Boolean, default=False)


class Account(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, nullable=False, unique=True)
    password = db.Column(db.String(64), nullable=False)
    is_active = db.Column(db.Boolean, default=True)

