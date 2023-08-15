#!/usr/bin/env python3
"""
Basic Flask application
"""

from flask import Flask, jsonify, request, make_response, abort
from auth import Auth


AUTH = Auth()
app = Flask(__name__)


@app.route('/', methods=["GET"])
def welcome():
    """
    Returns message when route requested
    """
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=["POST"])
def users():
    """
    Registers a new user
    """
    email = request.form.get('email')
    password = request.form.get('password')
    try:
        user = AUTH.register_user(email, password)
        return jsonify({"email": email, "message": "user created"})
    except ValueError:
        return jsonify({"message": "email already registered"})


@app.route('/sessions', methods=["POST"])
def sessions():
    """
    Creates a new session for the user, store it the session ID
    as a cookie with key "session_id" on the response and
    return a JSON payload of the form
    """
    email = request.form.get('email')
    password = request.form.get('password')
    if not AUTH.valid_login(email, password):
        abort(401)
    session_id = AUTH.create_session(email)
    if not session_id:
        abort(401)
    response = make_response(jsonify({"email": email, "message": "logged in"}))
    response.set_cookie("session_id", session_id)
    return response


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
