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
import game_controller

app = Flask(__name__, static_url_path="/static")
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


@app.route("/")
def home():
    if "username" not in session:
        return redirect("/login")


@app.route("/login")
def login_page():
    return send_from_directory("static", "login.html")


@app.route("/api/login", methods=["POST"])
def login():
    print(request.get_json())
    data = request.get_json()
    session["username"] = data["username"]
    new_url = f"/{data['game_ID']}"
    return redirect(new_url)


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
