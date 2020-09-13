from flask import Flask, Response, request, url_for, send_file, send_from_directory, jsonify
from flask_restful import Resource, Api
from game import Game as Game

app = Flask(__name__, static_url_path='/static')
api = Api(app)

g = Game()

@app.route('/')
def home():
    return send_from_directory('static', 'index.html')

@app.route('/static/script.js')
def script():
    return send_file('script.js')

@app.route('/static/styles.css')
def style():
    return send_from_directory('static','styles.css')

@app.route('/api/loadwords')
def get_words():
    global g
    return jsonify(g.words)

@app.route('/api/')
def get_revealed_words():
    global g
    return jsonify(g.words)

if __name__ == '__main__':
    app.debug = True
    app.run()
