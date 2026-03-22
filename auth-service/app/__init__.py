from flask import Flask
from app.config import Config
from app.db import mysql
from app.routes.auth_routes import auth_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    mysql.init_app(app)
    
    app.register_blueprint(auth_bp, url_prefix="/api/auth")
    
    @app.get("/health")
    def health():
        return {"status": "ok", "service": "auth-service"}
    
    return app