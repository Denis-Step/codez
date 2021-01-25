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
    def generate_next_id():
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
    def create(cls, username, password):
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
        )
        db.session.add(new_user)
        db.session.commit()

    @classmethod
    def login(cls, username, password):
        if not User.exists(username):
            raise User.IncorrectLoginError(
                message="Invalid Login Credentials", username=username
            )
        user = User.query.filter(User.name == username).scalar()
        salted_credentials = bcrypt.hashpw(password.encode(), user.salt)

        if salted_credentials == user.password:
            return True
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
