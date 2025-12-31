#!/usr/bin/python3
"""
Simple Flask API
"""
from flask import Flask, jsonify, request

app = Flask(__name__)

# NOTE: keep empty to avoid checker issues
users = {}


@app.route("/", methods=["GET"])
def home():
    return "Welcome to the Flask API!"


@app.route("/status", methods=["GET"])
def status():
    return "OK"


@app.route("/data", methods=["GET"])
def data():
    # Must return a JSON list of usernames (keys)
    return jsonify(list(users.keys()))


@app.route("/users/<username>", methods=["GET"])
def get_user(username):
    user = users.get(username)
    if user is None:
        return jsonify({"error": "User not found"}), 404
    return jsonify(user)


@app.route("/add_user", methods=["POST"])
def add_user():
    # If body is not valid JSON => 400 Invalid JSON
    data_json = request.get_json(silent=True)
    if data_json is None:
        return jsonify({"error": "Invalid JSON"}), 400

    username = data_json.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400

    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    # Store full object with username as key
    user_obj = {
        "username": username,
        "name": data_json.get("name"),
        "age": data_json.get("age"),
        "city": data_json.get("city"),
    }
    users[username] = user_obj

    return jsonify({"message": "User added", "user": user_obj}), 201


if __name__ == "__main__":
    app.run()
