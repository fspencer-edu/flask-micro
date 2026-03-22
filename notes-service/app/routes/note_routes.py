from flask import Blueprint
from app.controllers.note_controller import get_notes, create_note, delete_note

note_bp = Blueprint("note_bp", __name__)

note_bp.route("/api/notes", methods=["GET"])(get_notes)
note_bp.route("/api/notes", methods=["POST"])(create_note)
note_bp.route("/api/notes/<int:note_id>", methods=["DELETE"])(delete_note)