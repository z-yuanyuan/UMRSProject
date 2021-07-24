from flask import Flask  # include the flask library

app = Flask(__name__)


@app.route("/")
def index():
    return "Hello."


if __name__ == '__main__':
    app.run(port=5000, debug=True)