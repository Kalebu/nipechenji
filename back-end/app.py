import os
from flask import Flask, request
from models.database import db, Users


app = Flask(__name__)
app.secret_key = "codesucks"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)


def initialize_db():
    with app.app_context():
        if not os.path.isfile("database.db"):
            db.create_all()


initialize_db()


def get_bool_role(role):
    role_maper = {"provider": True, "consumer": False}
    return role_maper.get(role.lower())


@app.route("/")
def index():
    return {"hello": "Damn"}


@app.route("/signup", methods=["POST"])
def signup():

    user_data = request.get_json()
    name = user_data.get("name")
    phone = user_data.get("phone")
    location = user_data.get("location")
    role = user_data.get("role")
    password = user_data.get("password")
    role = get_bool_role(role)

    if all(name, phone, location, role):
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


@app.route("/signin")
def signin():
    signin_data = request.get_json()
    if signin_data:
        phone = signin_data.get("phone")
        password = signin_data.get("password")

        user_exists = Users.query.filter_by(phone=phone).first()
        if user_exists.is_authenticated(password):
            return {"loggedin": True}
    return {"loggedin": False}


if __name__ == "__main__":
    app.debug = True
    app.run(port=5000)