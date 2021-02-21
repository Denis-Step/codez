from flask import Flask, Blueprint, make_response, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api, Resource
from flask_jwt import JWT, jwt_required, current_identity
from models import models
from game import services, exceptions

codez_bp = Blueprint("codez_bp", __name__)
api = Api(codez_bp)


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

    @jwt_required()
    def post(self, game_id=None):
        data = request.get_json()
        if not game_id:
            state = services.create_game(data["ID"])
            return make_response(state, 201)

        services.handle_turn(game_id, data["team"], data["action"], data["payload"])
        return (None, 201)


def authenticate(username, password):
    try:
        return models.User.login(username, password)
    except Exception:
        return None


def identity(payload):
    user_id = payload["identity"]
    try:
        models.User.query.filter(models.User.id == user_id).scalar().id
    except Exception:
        return None


def create_app(db_path=None):
    app = Flask("Codez", static_folder="../static")
    app.debug = True
    api.add_resource(UserResource, "/users/<int:user_id>", "/users")
    api.add_resource(GameResource, "/games/<string:game_id>", "/games")
    app.register_blueprint(codez_bp)
    jwt = JWT(app, authenticate, identity)
    if db_path == None:
        db_path = "sqlite:///:memory"
    app.config["SQLALCHEMY_DATABASE_URI"] = db_path
    db = SQLAlchemy(app)
    db.init_app(app)
    return app