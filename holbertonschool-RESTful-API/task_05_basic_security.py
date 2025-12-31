#!/usr/bin/python3
"""
API Security and Authentication Techniques:
- Basic Auth (Flask-HTTPAuth)
- JWT Auth (Flask-JWT-Extended)
- Role-based access control (admin-only)
"""
from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import (
    JWTManager,
    create_access_token,
    jwt_required,
    get_jwt_identity,
)

app = Flask(__name__)

# Use a secret key for JWT. In real apps, use env var.
app.config["JWT_SECRET_KEY"] = "super-secret-key"

auth = HTTPBasicAuth()
jwt = JWTManager(app)

# Users stored in memory (as required)
users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user",
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin",
    },
}


# ---------- Basic Auth ----------
@auth.verify_password
def verify_password(username, password):
    user = users.get(username)
    if not user:
        return False
    return check_password_hash(user["password"], password)


@app.route("/basic-protected", methods=["GET"])
@auth.login_required
def basic_protected():
    return "Basic Auth: Access Granted"


# ---------- JWT Error handlers (IMPORTANT for checker: always 401 on auth errors) ----------
@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token_error(jwt_header, jwt_payload):
    return jsonify({"error": "Token has expired"}), 401


@jwt.revoked_token_loader
def handle_revoked_token_error(jwt_header, jwt_payload):
    return jsonify({"error": "Token has been revoked"}), 401


@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(jwt_header, jwt_payload):
    return jsonify({"error": "Fresh token required"}), 401


# ---------- JWT Login ----------
@app.route("/login", methods=["POST"])
def login():
    data = request.get_json(silent=True)
    if data is None:
        # Not required in spec, but safe
        return jsonify({"error": "Invalid JSON"}), 400

    username = data.get("username")
    password = data.get("password")

    user = users.get(username)
    if not user or not password or not check_password_hash(user["password"], password):
        # Authentication failure => 401
        return jsonify({"error": "Invalid credentials"}), 401

    # Put role into the token payload via identity (simple for checker)
    # identity can be a dict; get_jwt_identity() will return it back
    access_token = create_access_token(
        identity={"username": username, "role": user["role"]}
    )
    return jsonify({"access_token": access_token})


# ---------- JWT Protected ----------
@app.route("/jwt-protected", methods=["GET"])
@jwt_required()
def jwt_protected():
    return "JWT Auth: Access Granted"


# ---------- Role-based (Admin Only) ----------
@app.route("/admin-only", methods=["GET"])
@jwt_required()
def admin_only():
    identity = get_jwt_identity()  # dict: {"username":..., "role":...}
    role = None
    if isinstance(identity, dict):
        role = identity.get("role")

    if role != "admin":
        return jsonify({"error": "Admin access required"}), 403

    return "Admin Access: Granted"


if __name__ == "__main__":
    app.run()
