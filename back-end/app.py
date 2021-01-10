import os
import random
import hashlib
from flask_cors import CORS
from flask import Flask, request
from models.database import db, Users, Provider, Consumer


app = Flask(__name__)
app.secret_key = "codesucks"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)
CORS(app)


def initialize_db():
    with app.app_context():
        if not os.path.isfile("database.db"):
            db.create_all()


def create_token_string():
    token_string = "hvjsj{}ahah".format(random.randint(40000, 80000))
    token_string = token_string.encode("utf-8")
    return hashlib.sha256(token_string).hexdigest()


initialize_db()


def get_bool_role(role):
    if isinstance(role, str):
        role_maper = {"provider": True, "consumer": False}
        return role_maper.get(role.lower())
    raise TypeError("{} should be string not {}".format(role, type(role)))


@app.route("/")
def index():
    return {"hello": "Damn"}


@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        user_data = request.get_json()["data"]
        print(user_data)
        if user_data:
            name = user_data.get("name")
            phone = user_data.get("phone")
            location = user_data.get("location")
            role = user_data.get("role")
            password = user_data.get("password")
            role = get_bool_role(role)

            if all([name, phone, location, role]):
                new_user = Users(
                    name=name,
                    phone=phone,
                    location=location,
                    is_provider=role,
                    password=password,
                )
                db.session.add(new_user)
                db.session.commit()
                return {"user_added": True}
    return {"user_added": False}


@app.route("/signin", methods=["POST", "GET"])
def signin():
    if request.method == "POST":

        signin_data = request.get_json()
        if signin_data:
            phone = signin_data.get("phone")
            password = signin_data.get("password")
            user_exists = Users.query.filter_by(phone=phone).first()
            if user_exists.is_authenticated(password):
                token = create_token_string()
                user_exists.token = token
                db.session.add(user_exists)
                db.session.commit()
                return {"Token": token}
    return {"response": False}


@app.route("/add-consumer", methods=["GET", "POST"])
def add_consumer():
    if request.method == "POST":

        if request.get_json():
            consumer_data = request.get_json()
            token = consumer_data.get("token")
            if token:
                user_with_token = Users.query.filter_by(token=token).first()
                if user_with_token:
                    amount = consumer_data.get("amount")
                    location = consumer_data.get("location")
                    new_consumer = Consumer(
                        user_id=user_with_token.user_id,
                        phone=user_with_token.phone,
                        amount=amount,
                        location=location,
                    )
                    db.session.add(new_consumer)
                    db.session.commit()
                    return {"reponse": True}
    return {"reponse": False}


@app.route("/toa-chenji", methods=["GET", "POST"])
def add_provider():
    if request.method == "POST":
        if request.get_json():
            provider_data = request.get_json()
            token = provider_data.get("token")
            if token:
                user_with_token = Users.query.filter_by(token=token).first()
                if user_with_token:
                    consumer_phone = provider_data.get("consumer_phone")
                    main_consumer = Users.query.filter_by(phone=consumer_phone).first()
                    main_consumer.amepeta_chenji = True
                    db.session.add(main_consumer)
                    db.session.commit()
                    return {"reponse": "Chenji Imetolewa"}
    return {"response": "Could not process your request"}


if __name__ == "__main__":
    app.debug = True
    app.run(port=5000)