from flask import Flask, Blueprint, make_response
from flask_sqlalchemy import SQLAlchemy
from models import models

user_bp = Blueprint("user_bp", __name__)


@user_bp.route("/hello")
def test():
    return make_response("Worked", 200)


def create_app(db_path=None):
    app = Flask(__name__, static_url_path="/static")
    app.register_blueprint(user_bp)
    if db_path == None:
        db_path = "sqlite:///:memory"
    app.config["SQLALCHEMY_DATABASE_URI"] = db_path
    db = SQLAlchemy(app)
    db.init_app(app)
    return app