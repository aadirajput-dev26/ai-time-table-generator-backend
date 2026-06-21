from flask import Blueprint, jsonify

health_check_bp = Blueprint("health-check", __name__)

@health_check_bp.route("/health-check", methods=["GET"])
def health_check():
    return jsonify({
        "success" : True,
        "status" : "healthy",
        "message" : "Backend Server running....."
    }), 200