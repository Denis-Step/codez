import bcrypt
import datetime
import jwt
from nltk.corpus import wordnet as wn
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

    @staticmethod
    def get(text):
        word = Word.query.filter(Word.word == text).scalar()
        return word

    @staticmethod
    def common_hypernyms(first_word, second_word):
        common_hyps = set()

        for syn in wn.synsets(first_word):
            for syn2 in wn.synsets(second_word):
                com = syn.common_hypernyms(syn2)
                for comSyn in com:
                    common_hyps.add(comSyn.name())

        return common_hyps

    def definitions(self):
        synset = wn.synsets(self.word)
        definitions = {syn.name(): syn.definition() for syn in synset}
        return definitions


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String)
    password = db.Column(db.String, nullable=False)
    salt = db.Column(db.String, nullable=False)
    gamesPlayed = db.Column(db.Integer)
    gamesWon = db.Column(db.Integer)

    class UserExistsError(Exception):
        def __init__(self, message, username):
            super().__init__(message)
            self.username = username

    class IncorrectLoginError(Exception):
        def __init__(self, message, username):
            super().__init__(message)
            self.username = username

    def __repr__(self):
        return f"User {self.name}"

    @staticmethod
    def get(ID):
        user = User.query.filter(User.id == ID).scalar()
        return user

    @staticmethod
    def generate_next_id():
        if User.query.count() == 0:
            return 0
        highest_id = User.query.order_by(User.id.desc()).first().id
        return highest_id + 1

    @staticmethod
    def hash_password(password):
        salt = bcrypt.gensalt()
        hashed_pw = bcrypt.hashpw(password.encode(), salt)
        return {"salt": salt, "hashed_pw": hashed_pw}

    @classmethod
    def exists(cls, username):
        user = User.query.filter(User.name == username).scalar()
        return bool(user)

    @classmethod
    def create(cls, username, password, **kwargs):
        if User.exists(username):
            raise User.UserExistsError(
                message="Username already exists", username=username
            )

        pw_info = User.hash_password(password)
        new_user = User(
            id=User.generate_next_id(),
            name=username,
            password=pw_info["hashed_pw"],
            salt=pw_info["salt"],
            **kwargs,
        )
        db.session.add(new_user)
        db.session.commit()
        return new_user

    @classmethod
    def login(cls, username, password):
        if not User.exists(username):
            raise User.IncorrectLoginError(
                message="Invalid Login Credentials", username=username
            )
        user = User.query.filter(User.name == username).scalar()
        salted_credentials = bcrypt.hashpw(password.encode(), user.salt)

        if salted_credentials == user.password:
            return user
        else:
            raise User.IncorrectLoginError(
                message="Invalid Login Credentials", username=username
            )


class GameHistory(db.Model):
    __tablename__ = "gamehistories"

    gamehistoryid = db.Column(db.String, primary_key=True)
    history = db.Column(db.String)
    winners = db.Column(db.String)
    date = db.Column(db.String)

    def __repr__(self):
        return f"{self.gamehistoryid}"
