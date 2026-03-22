import datetime
import jwt
from flask import current_app

def generate_token(user_id):
    payload = {
        "user_id": user_id,
        "exp": datetime.datetime.now() + datetime.timedelta(hours=24)
    }
    return jwt.encode(payload, current_app.config["SECRET_KEY"], algorithm="HS256")

def verify_token(token):
    try:
        return jwt.decode(token, current_app.config["SECRET_KEY"], algorithms="HS256")
    except Exception:
        return None