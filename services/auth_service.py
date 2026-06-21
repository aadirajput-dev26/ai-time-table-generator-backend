from services import db_dash_service
from config import settings
from utils.jwt_utils import generate_token, decode_token

def signup_user(name: str, email: str, password: str, role: str):
    try:
        existing = db_dash_service.get_record(settings.AUTH_TABLE_ID, f"email='{email}'")
        rows = existing.get("data", {}).get("rows", [])

        if rows:  # if any rows exist, email is already registered
            return {"success": False, "message": "Email already registered"}

        payload = {
            "name": name,
            "email": email,
            "password": password,
            "role": role,
            "is_active": True
        }
        result = db_dash_service.create_record(settings.AUTH_TABLE_ID, payload)

        user_id = result.get("data", {}).get("data", {}).get("rowid")
        role = result.get("data", {}).get("data", {}).get("role")
        email = result.get("data", {}).get("data", {}).get("email")

        token = generate_token(user_id, email, role)
        return {"success": True, "message": "User registered successfully", "data": result, "token" : token}

    except Exception as e:
        return {"success": False, "message": f"Internal error: {str(e)}"}

def login_user(email: str, password: str):
    try:
        existing = db_dash_service.get_record(
            settings.AUTH_TABLE_ID,
            f"email='{email}' AND password='{password}'"
        )
        rows = existing.get("data", {}).get("rows", [])

        if not rows:
            return {"success": False, "message": "Invalid credentials"}

        user = rows[0]
        token = generate_token(user["rowid"], user["email"], user["role"])  # <-- FIXED

        return {
            "success": True,
            "message": "Login successful",
            "token": token,
            "user": {
                "id": user["rowid"],
                "email": user["email"],
                "role": user["role"]
            }
        }

    except Exception as e:
        return {"success": False, "message": f"Internal error: {str(e)}"}
