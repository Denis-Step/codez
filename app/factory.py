import os
import json
from flask import Flask, Blueprint, send_file, request, redirect, url_for, Response
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from flask_login import (
    LoginManager,
    current_user,
    login_required,
    login_user,
    logout_user,
)
from oauthlib.oauth2 import WebApplicationClient
import requests
from models import models
from resources import UserResource, GameResource, DefinitionResource, HypernymResource

# Configuration
GOOGLE_CLIENT_ID = os.environ.get("GOOGLE_CLIENT_ID", None)
GOOGLE_CLIENT_SECRET = os.environ.get("GOOGLE_CLIENT_SECRET", None)
GOOGLE_DISCOVERY_URL = "https://accounts.google.com/.well-known/openid-configuration"


codez_bp = Blueprint("codez_bp", __name__)
api = Api(codez_bp)


login_manager = LoginManager()
client = WebApplicationClient(GOOGLE_CLIENT_ID)


@login_manager.user_loader
def load_user(user_id):
    return models.User.get(user_id)


@codez_bp.route("/static/script.js")
def dev_spa_script():
    return send_file("../client/dist/script.js")


@codez_bp.route("/static/login.js")
def login_page():
    return send_file("../client/dist/login.js")


@codez_bp.route("/login")
def login():
    # Find out what URL to hit for Google login
    google_provider_cfg = get_google_provider_cfg()
    authorization_endpoint = google_provider_cfg["authorization_endpoint"]

    request_uri = client.prepare_request_uri(
        authorization_endpoint,
        redirect_uri=request.base_url + "/callback",
        scope=["openid", "email", "profile"],
    )
    return redirect(request_uri)


@codez_bp.route("/login/callback")
def callback():
    code = request.args.get("code")

    google_provider_cfg = get_google_provider_cfg()
    token_endpoint = google_provider_cfg["token_endpoint"]

    token_url, headers, body = client.prepare_token_request(
        token_endpoint,
        authorization_response=request.url,
        redirect_url=request.base_url,
        code=code,
    )
    token_response = requests.post(
        token_url,
        headers=headers,
        data=body,
        auth=(GOOGLE_CLIENT_ID, GOOGLE_CLIENT_SECRET),
    )

    client.parse_request_body_response(json.dumps(token_response.json()))

    userinfo_endpoint = google_provider_cfg["userinfo_endpoint"]
    uri, headers, body = client.add_token(userinfo_endpoint)
    userinfo_response = requests.get(uri, headers=headers, data=body)

    if userinfo_response.json().get("email_verified"):
        unique_id = userinfo_response.json()["sub"]
        user_email = userinfo_response.json()["email"]
        user_name = userinfo_response.json()["given_name"]
        # picture = userinfo_response.json()["picture"]
    else:
        return Response("User email not available or not verified by Google.", 400)

    if models.User.email_exists(user_email):
        user = models.User.query.filter(models.User.email == user_email).scalar()
    else:
        user = models.User.create(
            username=user_name,
            password=models.User.random_password(20),
            email=user_email,
        )

    login_user(user)
    print(user)
    return redirect(url_for("codez_bp.index"))


@codez_bp.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("index"))


# Catch-all
@codez_bp.route("/", defaults={"path": ""})
@codez_bp.route("/<path:path>")
def index(path):
    if not current_user.is_authenticated:
        return send_file("../static/login.html")
    return send_file("../static/index.html")


def get_google_provider_cfg():
    return requests.get(GOOGLE_DISCOVERY_URL).json()


def create_app(db_path=None):
    app = Flask("Codez", static_folder="../static")
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
    login_manager.init_app(app)
    return app