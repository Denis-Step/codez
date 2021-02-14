from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from models import models


def create_app(db_path=None):
    app = Flask(__name__, static_url_path="/static")
    if db_path == None:
        db_path = "sqlite:///:memory"
    app.config["SQLALCHEMY_DATABASE_URI"] = db_path
    db = SQLAlchemy(app)
    db.init_app(app)
    return app
