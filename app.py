from flask import Flask

app = Flask(__name__)

@app.route("/")
def welcome():
    return "Hello"

@app.route("/home")
def home():
    return "This is home page"

import controller.signup as signup


if __name__ == '__main__':
    app.run(debug=True)