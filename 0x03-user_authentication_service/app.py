#!/usr/bin/env python3
"""module for implementing user module functionalities"""
from flask import Flask, jsonify, request
from auth import Auth


AUTH = Auth()
app = Flask(__name__)


@app.route('/', methods=['GET'], strict_slashes=False)
def bienvenue():
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=['POST'], strict_slashes=False):
def users():
    """method to register users"""
    print(request.form)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
