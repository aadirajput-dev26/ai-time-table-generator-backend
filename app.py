from flask import Flask, jsonify
from routes.auth_routes import auth_bp
from routes.health_check_routes import health_check_bp

app = Flask(__name__)

app.register_blueprint(auth_bp, url_prefix="/api/v1/auth")
app.register_blueprint(health_check_bp, url_prefix="/api/v1")

if __name__ == "__main__":
    app.run(debug=True)
