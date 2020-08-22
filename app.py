from flask import Flask, Response, request, url_for, send_file, send_from_directory
app = Flask(__name__, static_url_path='/static')


@app.route('/')
def home():
    return send_from_directory('static', 'index.html')


@app.route('/static/script.js')
def script():
    return send_file('script.js')

@app.route('/static/style.css')
def style():
    return send_file('style.css')


if __name__ == '__main__':
    app.debug = True
    app.run()
