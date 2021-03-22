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
from models import models
from game import services, exceptions
from resources import UserResource, GameResource, DefinitionResource, HypernymResource

# Configuration
GOOGLE_CLIENT_ID = os.environ.get("GOOGLE_CLIENT_ID", None)
GOOGLE_CLIENT_SECRET = os.environ.get("GOOGLE_CLIENT_SECRET", None)
GOOGLE_DISCOVERY_URL = "https://accounts.google.com/.well-known/openid-configuration"

login_manager = LoginManager()

codez_bp = Blueprint("codez_bp", __name__)
api = Api(codez_bp)
login_manager = LoginManager()


@codez_bp.route("/static/script.js")
def dev_spa_script():
    return send_file("../client/dist/script.js")


# Catch-all
@codez_bp.route("/", defaults={"path": ""})
@codez_bp.route("/<path:path>")
def index(path):
    return send_file("../static/index.html")


def authenticate(username, password):
    try:
        return models.User.login(username, password)
    except Exception:
        return None


def create_app(db_path=None):
    app = Flask("Codez", static_folder="../static")
    app.debug = True
    api.add_resource(UserResource, "/users/<int:user_id>", "/users/")
    api.add_resource(GameResource, "/games/<string:game_id>", "/games/")
    api.add_resource(DefinitionResource, "/definitions/<string:word>")
    api.add_resource(HypernymResource, "/hypernyms")
    app.register_blueprint(codez_bp)
    if db_path is None:
        db_path = "sqlite:///db.db"
    else:
        db_path = "sqlite:///" + db_path
    app.config["SQLALCHEMY_DATABASE_URI"] = db_path
    app.config["SECRET_KEY"] = os.environ.get("FLASK_SECRET_KEY")
    db = SQLAlchemy(app)
    db.init_app(app)
    return app