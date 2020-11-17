from flask import Flask, Response, request, url_for, send_file, send_from_directory, jsonify, make_response
from flask_restful import Resource, Api
from game import Game as Game
import services

app = Flask(__name__, static_url_path='/static')
api = Api(app)


@app.route('/')
def home():
    return send_from_directory('static', 'index.html')


@app.route('/<game_ID>')
def game_view(game_ID):
    return send_from_directory('static', 'index.html')


@app.route('/static/script.js')
def script():
    return send_file('script.js')


@app.route('/static/styles.css')
def style():
    return send_from_directory('static', 'styles.css')


@app.route('/<game_ID>/loadwords')
def get_words(game_ID):
    words = services.get_state(game_ID)
    return jsonify(words)


'''@app.route('/api/revealword', methods=['GET', 'POST'])
def get_revealed_words():
    global g

    if request.method == 'POST':
        word = request.get_json()['pick']
        g.reveal_word(word)
        data = {'message': 'Created', 'code': 'SUCCESS'}
        return make_response(jsonify(data), 201)'''

if __name__ == '__main__':
    app.debug = True
    app.run()
