from flask import Flask, Blueprint, make_response, request
from flask_sqlalchemy import SQLAlchemy
from models import models
from flask_restful import Api, Resource

codez_bp = Blueprint("codez_bp", __name__)
api = Api(codez_bp)


class UserResource(Resource):
    def get(self, id):
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
    def get(self, id):
        pass


def create_app(db_path=None):
    app = Flask(__name__, static_url_path="/static")
    api.add_resource(UserResource, "/users/<int:id>", "/users")
    app.register_blueprint(codez_bp)
    if db_path == None:
        db_path = "sqlite:///:memory"
    app.config["SQLALCHEMY_DATABASE_URI"] = db_path
    db = SQLAlchemy(app)
    db.init_app(app)
    return app