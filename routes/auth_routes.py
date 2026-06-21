from flask import Blueprint, request, jsonify
from services import auth_service

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/signup", methods=["POST"])
def user_signup():
    data = request.json
    result = auth_service.signup_user(
        data.get("name"),
        data.get("email"),
        data.get("password"),
        data.get("role")
    )

    if result["success"]:
        return jsonify(result), 201  # Created
    elif result["message"] == "Email already registered":
        return jsonify(result), 400  # Bad Request
    else:
        return jsonify(result), 500  # Internal Server Error

@auth_bp.route("/login", methods=["POST"])
def user_login():
    data = request.json
    result = auth_service.login_user(
        data.get("email"),
        data.get("password")
    )
    if result["success"]:
        return jsonify(result), 200
    else:
        return jsonify(result), 401