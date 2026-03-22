from flask import jsonify, request
from app.utils.redis_client import redis_client

def get_notes():
    keys = sorted(redis_client.keys("note:*"))
    notes = []

    for key in keys:
        note_id = key.split(":")[1]
        notes.append({
            "id": int(note_id),
            "text": redis_client.get(key)
        })

    return jsonify({"notes": notes}), 200

def create_note():
    data = request.get_json(silent=True) or {}
    text = data.get("text", "").strip()

    if not text:
        return jsonify({"error": "text is required"}), 400

    note_id = redis_client.incr("next_note_id")
    redis_client.set(f"note:{note_id}", text)

    return jsonify({"id": note_id, "text": text}), 201

def delete_note(note_id):
    deleted = redis_client.delete(f"note:{note_id}")
    if not deleted:
        return jsonify({"error": "note not found"}), 404
    return jsonify({"message": "deleted"}), 200