from flask_login import UserMixin
from datetime import datetime
from . import db

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True) #primary key field required in SQLAlchemy
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(100))

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True) #primary key field required in SQLAlchemy
    title = db.Column(db.String(100))
    content = db.Column(db.String(1000))
    # created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
