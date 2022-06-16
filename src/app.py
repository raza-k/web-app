from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/')
def index():
    return '<h1>OK</h1>'


@app.route('/quote')
def quote():

    return {
        "id": 0,
        "quote": "A quick brown fox jumps over a lazy dog"
    }


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
