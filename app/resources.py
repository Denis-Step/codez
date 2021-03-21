from flask import make_response, request, jsonify
from flask_restful import Resource
from models import models
from game import services, exceptions


class UserResource(Resource):
    # TODO: FIX THIS
    def get(self, user_id):
        return make_response("Working", 200)

    def post(self):
        data = request.get_json()
        if data["action"] == "signup":
            try:
                models.User.create(username=data["username"], password=data["password"])
                return make_response("Created User", 201)
            except models.User.UserExistsError:
                return make_response("User Exists", 400)

        elif data["action"] == "login":
            try:
                models.User.login(username=data["username"], password=data["password"])
                return make_response("Logged in", 200)
            except models.User.IncorrectLoginError:
                return make_response("Credentials not Found", 401)


class GameResource(Resource):
    def get(self, game_id):
        try:
            state = services.get_state(game_id)
            for word, value in state["wordsState"].items():
                if value not in ("blue-revealed", "red-revealed"):
                    state["wordsState"][word] = "hidden"
            return jsonify(state)
        except exceptions.GameNotFoundError:
            return make_response("Game Not Found", 404)

    def post(self, game_id=None):
        data = request.get_json()
        if not game_id:
            if data["action"] == "create":
                state = services.create_game(data["payload"]["gameID"])
                return make_response(state, 201)

        services.handle_turn(game_id, data["team"], data["action"], data["payload"])
        return (None, 201)


class DefinitionResource(Resource):
    def get(self, word):
        return jsonify(models.Word.get(word).definitions())
