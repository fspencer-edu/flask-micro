from flask import Flask
from app.routes.note_routes import note_bp

def create_app():
    app = Flask(__name__)
    app.register_blueprint(note_bp)

    @app.get("/health")
    def health():
        return {"status": "ok", "service": "notes-service"}

    return app