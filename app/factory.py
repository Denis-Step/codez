from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from models import models


def create_app():
    app = Flask(__name__, static_url_path="/static")
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.db"
    db = SQLAlchemy(app)
    db.init_app(app)
    return app
