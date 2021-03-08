import os
from flask import Flask, Blueprint, make_response, request, jsonify, send_file
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api, Resource
from flask_login import (
    LoginManager,
    current_user,
    login_required,
    login_user,
    logout_user,
)
from oauthlib.oauth2 import WebApplicationClient
from models import models
from game import services, exceptions

# Configuration
GOOGLE_CLIENT_ID = os.environ.get("GOOGLE_CLIENT_ID", None)
GOOGLE_CLIENT_SECRET = os.environ.get("GOOGLE_CLIENT_SECRET", None)
GOOGLE_DISCOVERY_URL = "https://accounts.google.com/.well-known/openid-configuration"

login_manager = LoginManager()

codez_bp = Blueprint("codez_bp", __name__)
api = Api(codez_bp)
login_manager = LoginManager()


class UserResource(Resource):
    # TODO: FIX THIS
    def get(self, user_id):
        return make_response("Working", 200)

    def post(self):
        data = request.get_json()
        if data["action"] == "signup":
            try:
                models.User.create(username=data["username"], password=data["password"])
                return make_response("Created User", 201)
            except models.User.UserExistsError:
                return make_response("User Exists", 400)

        elif data["action"] == "login":
            try:
                models.User.login(username=data["username"], password=data["password"])
                return make_response("Logged in", 200)
            except models.User.IncorrectLoginError:
                return make_response("Credentials not Found", 401)


class GameResource(Resource):
    def get(self, game_id):
        try:
            state = services.get_state(game_id)
            for word, value in state["wordsState"].items():
                if value not in ("blue-revealed", "red-revealed"):
                    state["wordsState"][word] = "hidden"
            return jsonify(state)
        except exceptions.GameNotFoundError:
            return make_response("Game Not Found", 404)

    def post(self, game_id=None):
        data = request.get_json()
        if not game_id:
            state = services.create_game(data["ID"])
            return make_response(state, 201)

        services.handle_turn(game_id, data["team"], data["action"], data["payload"])
        return (None, 201)


@codez_bp.route("/")
def home_page():
    return send_file("../static/index.html")


@codez_bp.route("/static/script.js")
def dev_spa_script():
    return send_file("../client/dist/script.js")


def authenticate(username, password):
    try:
        return models.User.login(username, password)
    except Exception:
        return None


def identity(payload):
    user_id = payload["identity"]
    try:
        return models.User.query.filter(models.User.id == user_id).scalar().id
    except Exception:
        return None


# Flask-Login helper to retrieve a user from our db
@login_manager.user_loader
def load_user(user_id):
    return models.User.get(user_id)


def create_app(db_path=None):
    app = Flask("Codez", static_folder="../static")
    app.debug = True
    api.add_resource(UserResource, "/users/<int:user_id>", "/users")
    api.add_resource(GameResource, "/games/<string:game_id>", "/games")
    app.register_blueprint(codez_bp)
    if db_path is None:
        db_path = "sqlite:///db.db"
    else:
        db_path = "sqlite:///" + db_path
    app.config["SQLALCHEMY_DATABASE_URI"] = db_path
    app.config[
        "SECRET_KEY"
    ] = '\xfd{H\xe5<\x95\xf9\xe3\x96.5\xd1\x01O<!\xd5\xa2\xa0\x9fR"\xa1\xa8'
    db = SQLAlchemy(app)
    db.init_app(app)
    client = WebApplicationClient(GOOGLE_CLIENT_ID)
    login_manager.init_app(app)
    return app