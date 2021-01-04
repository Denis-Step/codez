import bcrypt
from flask_sqlalchemy import SQLAlchemy
from flask import Flask

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.db"
db = SQLAlchemy(app)


class Word(db.Model):
    __tablename__ = "words"

    word = db.Column(db.String, primary_key=True)
    wordid = db.Column(db.Integer)

    def __repr__(self):
        return f"{self.word}"


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    email = db.Column(db.String)
    password = db.Column(db.String, nullable=False)
    salt = db.Column(db.String, nullable=False)
    gamesPlayed = db.Column(db.Integer)
    gamesWon = db.Column(db.Integer)

    def __repr__(self):
        return f"User {self.name}"

    @classmethod
    def generate_next_id(cls):
        highest_id = User.query.order_by(User.id.desc())
        return highest_id + 1

    @classmethod
    def hash_password(cls, password):
        salt = bcrypt.gensalt()
        hashed_pw = bcrypt.hashpw(password, salt)
        return {"salt": salt, "hashed_pw": hashed_pw}


class GameHistory(db.Model):
    __tablename__ = "gamehistories"

    gamehistoryid = db.Column(db.String, primary_key=True)
    history = db.Column(db.String)
    winners = db.Column(db.String)
    date = db.Column(db.String)

    def __repr__(self):
        return f"{self.gamehistoryid}"
