from dataclasses import dataclass
from app import db


@dataclass
class Entry(db.Model):
    id: int
    title: str
    description: str
    status: bool

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64), index=True, nullable=False)
    description = db.Column(db.String(120), index=True, nullable=False)
    status = db.Column(db.Boolean, default=False)

@dataclass
class Profile(db.Model):
    id: int
    profile: str
    is_active: bool
    is_favorite: bool

    id = db.Column(db.Integer, primary_key=True)
    profile = db.Column(db.String(64), index=True, nullable=False, unique=True)
    is_active = db.Column(db.Boolean, default=True)
    is_favorite = db.Column(db.Boolean, default=False)

@dataclass
class Account(db.Model):
    id: int
    username: str
    password: str
    is_active: bool

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, nullable=False, unique=True)
    password = db.Column(db.String(64), nullable=False)
    is_active = db.Column(db.Boolean, default=True)

