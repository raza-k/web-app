from flask import Flask, request
from flask_cors import CORS
from datetime import datetime

app = Flask(__name__)
CORS(app)


@app.route('/')
def index():
    return '<h1>OKAY</h1>'


@app.route('/quote')
def quote():

    return {
        "id": 0,
        "quote": "A quick brown fox jumps over a lazy dog",
        "name": "Raza",
        "School": "CalHigh"
    }

@app.route('/time')
def time():
    today = datetime.now()
    return "Current date and time: " + today.strftime("%Y-%m-%d %H:%M %p")


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)
