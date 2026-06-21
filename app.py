from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/health-check", methods=["GET"])
def health_check():
    return jsonify({
        "success" : True,
        "status" : "healthy",
        "message" : "Backend Server running....."
    }), 200