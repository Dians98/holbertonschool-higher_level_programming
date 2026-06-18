#!/usr/bin/python3
from flask import Flask, request
from flask import jsonify

app = Flask(__name__)

# users = {"jane": {"name": "Jane", "age": 28, "city": "Los Angeles"}}


@app.route("/")
def home():
    return "Welcome to the Flask API!"


@app.route("/data")
def getData():
    return jsonify(list(users.keys()))


@app.route("/status")
def getStatus():
    return "OK"


@app.route('/user/<username>')
def getUsername(username):
    if username:
        return username
    else:
        msg = {"error": "User not found"}
        return jsonify(msg), 404


if __name__ == '__main__':
    app.run(debug=True)
