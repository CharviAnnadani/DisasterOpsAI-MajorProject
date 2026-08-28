from flask import Blueprint, request, jsonify

from models.sos_model import create_sos, get_all_sos
from services.priority_service import calculate_priority

sos_bp = Blueprint("sos", __name__)

@sos_bp.route("/sos", methods=["POST"])
def create_sos_request():

    data = request.get_json()

    name = data["name"]
    latitude = data["latitude"]
    longitude = data["longitude"]
    disaster_type = data["disaster_type"]

    priority = calculate_priority(disaster_type)

    create_sos(
        name,
        latitude,
        longitude,
        disaster_type,
        priority,
        "Pending"
    )

    return jsonify({
        "message": "SOS Request Created Successfully"
    })

@sos_bp.route("/sos", methods=["GET"])
def fetch_sos():

    data = get_all_sos()

    return jsonify(data)