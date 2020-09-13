from flask import Flask, Response, request, url_for, send_file, send_from_directory, jsonify
from flask_restful import Resource, Api

from game import Game as GameState

app = Flask(__name__, static_url_path='/static')
api = Api(app)

class Game(Resource):
    def __init__(self):
        super().__init__()
        self.currGame = None

    def get(self):
        if not isinstance(self.currGame,GameState):
            self.currGame = GameState()
            print(self.currGame.words)
        return jsonify(list(self.currGame.words.keys()))

api.add_resource(Game, '/loadWords')

@app.route('/')
def home():
    return send_from_directory('static', 'index.html')

@app.route('/static/script.js')
def script():
    return send_file('script.js')

@app.route('/static/styles.css')
def style():
    return send_from_directory('static','styles.css')

@app.route('/api/loadWords')
def load_words():
    words = []
    for i in range(0,25):
        words.append(str(i))
    return jsonify(words)

if __name__ == '__main__':
    app.debug = True
    app.run()
