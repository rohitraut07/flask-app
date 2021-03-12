from datetime import datetime

from main import db


class Subscription(db.Model):
    """ User Model for storing user related details """
    __tablename__ = "subscribers"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(120), unique=True)
    public_id = db.Column(db.String(100), unique=True)
    subscription = db.Column(db.Boolean, default=True)
    timestamp = db.Column(db.DateTime, default=datetime.now())

    def __init__(self, email, public_id):
        self.public_id = public_id
        self.email = email


class AdminUser(db.Model):
    """admin User"""
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(50), nullable=False)
    public_id = db.Column(db.String(100), unique=True)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(255), nullable=False, unique=True)
    password = db.Column(db.String(256), nullable=False)

    def __init__(self, first_name, last_name, public_id, email, password):
        self.first_name = first_name
        self.last_name = last_name
        self.public_id = public_id
        self.email = email
        self.password = password
