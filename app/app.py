from flask import (
    Flask,
    Response,
    request,
    url_for,
    send_file,
    send_from_directory,
    jsonify,
    make_response,
    abort,
    session,
    redirect,
)
from flask_sqlalchemy import SQLAlchemy
from game import game_controller
from models import models

app = Flask(__name__, static_url_path="/static")
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.db"
db = SQLAlchemy(app)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


@app.route("/")
def home():
    if "username" not in session:
        return redirect("/login")


@app.route("/login")
def login_page():
    return send_from_directory("../static", "login.html")


@app.route("/api/signup", methods=["POST"])
def signup():
    print(request.get_json())
    try:
        data = request.get_json()
        print(data)
        models.User.create(data["username"], data["password"])
        return make_response("Signed Up", 201)
    except models.User.UserExistsError:
        abort(400, "User Already Exists")


@app.route("/api/login", methods=["POST"])
def login():
    data = request.get_json()
    try:
        models.User.login(data["username"], data["password"])
        return make_response("Logged in", 200)
    except models.User.IncorrectLoginError:
        abort(400, "Incorrect Login Credentials")


@app.route("/static/script.js")
def main_script():
    return send_file("dist/script.js")


@app.route("/static/login.js")
def login_script():
    return send_file("dist/login.js")


@app.route("/static/styles.css")
def style():
    return send_from_directory("static", "styles.css")


@app.route("/<game_ID>")
def game_view(game_ID):
    return send_from_directory("static", "index.html")


@app.route("/<string:game_ID>/loadwords")
def get_words(game_ID):
    print(game_ID)
    words = game_controller.get_or_create_state(game_ID)
    return jsonify(words)


@app.route("/<string:game_ID>/spymaster", methods=["POST"])
def enter_hint(game_ID):
    if request.method != "POST":
        abort(400, "POST Data required")

    print(request.get_json())
    code = game_controller.check_turn(game_ID, "blue", "spymaster", request.get_json())
    if code == 0:
        abort(400, "Invalid")
    elif code == 1:
        return "Accepted"


@app.route("/<string:game_ID>/revealword", methods=["POST"])
def reveal_word(game_ID):
    if request.method != "POST":
        abort(400, "POST Data required")


if __name__ == "__main__":
    app.debug = True
    app.run()
