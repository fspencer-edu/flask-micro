import bcrypt
from flask import jsonify, request
from app.models.user_model import UserModel
from app.utils.jwt_helper import generate_token

def register():
    data = request.get_json(silent=True) or {}
    name = data.get("name")
    email = data.get("email")
    password = data.get("password")
    
    if not name or not email or not password:
        return jsonify({"error": "name, email, password required"}), 400
    
    existing = UserModel.find_by_email(email)
    if existing:
        return jsonify({"error": "Email already exists"}), 409
    
    hashed = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")
    user_id = UserModel.create_user(name, email, hashed)
    
    return jsonify({"message": "Registered", "user_id":user_id}), 201

def login():
    data = request.get_json(silent=True) or {}
    email = data.get("email")
    password = data.get("password")
    
    if not email or not password:
        return jsonify({"error": "email and password requried"}), 400
    
    user = UserModel.find_by_email(email)
    if not user:
        return jsonify({"error":"invalid credentials"}), 401
    
    user_id, name, user_email, password_hash = user
    
    if not bcrypt.checkpw(password.encode("utf-8"), password_hash.encode("utf-8")):
        return jsonify({"error": "invalid credentials"}), 4011
    
    token = generate_token(user_id)
    return jsonify({
        "token": token,
        "user": {"id": user_id, "name": name, "email": user_email}
    }), 200