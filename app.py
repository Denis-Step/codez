from flask import Flask, request, url_for
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


url_for('static', filename='style.css')


@app.route(url_for('static', filename='style.css'))
def show_static():
    return


@app.route('/<num>', methods=['GET', 'POST'])
def show_post(num):
    return f'The number is {num}!'


if __name__ == '__main__':
    app.debug = True
    app.run()
