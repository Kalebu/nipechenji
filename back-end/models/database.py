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
    token = db.Column(db.String(120), nullable=True)

    def __init__(self, **kwargs):
        super(Users, self).__init__(**kwargs)
        self.password = hashlib.sha256(self.password).hexdigest()

    def is_authenticated(self, new_password):
        return hashlib.sha256(new_password).hexdigest() == self.password

    def __repr__(self):
        return "<User> {}".format(self.name)

    def __str__(self):
        return "<User> {}".format(self.name)


class Consumer(db.Model):
    __tablename__ = "consumers"

    consumer_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"))
    phone = db.Column(db.String(50), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    location = db.Column(db.String(50), nullable=False)
    amepeta_chenji = db.Column(db.Boolean, default=False)
    users = db.relationship(Users)

    def __repr__(self):
        return "<Consumer> {}".format(self.consumer_id)

    def __str__(self):
        return "<Consumer> {}".format(self.consumer_id)


class Provider(db.Model):
    __tablename__ = "provider"

    provider_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"))
    phone = db.Column(db.String(50), nullable=False)
    ana_chenji = db.Column(db.Boolean, nullable=False)
    users = db.relationship(Users)

    def __repr__(self):
        return "<Provider> {}".format(self.provider_id)

    def __str__(self):
        return "<Provider> {}".format(self.provider_id)