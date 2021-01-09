import hashlib
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class Users(db.Model):
    __tablename__ = "users"

    user_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.String(40), nullable=False)
    location = db.Column(db.String(50), nullable=True)
    password = db.Column(db.String(60), nullable=False)
    is_provider = db.Column(db.Boolean, nullable=False)

    def __init__(self, **kwargs):
        super(Users, self).__init__(**kwargs)
        self.password = hashlib.sha256(self.password).hexdigest()

    def is_authenticated(self, new_password):
        return hashlib.sha256(new_password).hexdigest() == self.password
