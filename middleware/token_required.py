from flask import request, jsonify
from functools import wraps
from utils.jwt_utils import decode_token

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if "Authorization" in request.headers:
            token = request.headers["Authorization"].split(" ")[1]  # Bearer <token>

        if not token:
            return jsonify({"success": False, "message": "Token missing"}), 401

        data = decode_token(token)
        if not data:
            return jsonify({"success": False, "message": "Token invalid/expired"}), 401

        return f(data, *args, **kwargs)  # pass decoded payload to route
    return decorated
