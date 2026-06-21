import jwt
import datetime
from config import settings

SECRET_KEY = settings.JWT_SECRET  # put your secret in config.py

def generate_token(user_id: str, email: str, role: str):
    payload = {
        "id": user_id,
        "email": email,
        "role": role,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1)
    }
    return jwt.encode(payload, SECRET_KEY, algorithm="HS256")

def decode_token(token: str):
    try:
        return jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None
