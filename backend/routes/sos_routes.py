from flask import Blueprint, request, jsonify

from models.sos_model import (
    create_sos,
    get_all_sos,
    update_sos_status,
    delete_sos,
    get_dashboard_stats
)

from services.priority_service import (
    calculate_priority,
    assign_rescue_team
)

sos_bp = Blueprint("sos", __name__)


@sos_bp.route("/sos", methods=["POST"])
def create_sos_request():

    data = request.get_json()

    name = data["name"]
    phone = data["phone"]
    location = data["location"]
    disaster_type = data["disaster_type"]
    description = data["description"]

    priority = calculate_priority(
        disaster_type,
        description
    )

    assigned_team = assign_rescue_team(
        disaster_type
    )

    create_sos(
        name,
        phone,
        location,
        disaster_type,
        description,
        priority,
        assigned_team,
        "Team Assigned"
    )

    return jsonify({
        "message": "SOS Request Created Successfully",
        "priority": priority,
        "assigned_team": assigned_team
    })


@sos_bp.route("/sos", methods=["GET"])
def fetch_sos():

    return jsonify(get_all_sos())


@sos_bp.route("/dashboard", methods=["GET"])
def dashboard():

    return jsonify(get_dashboard_stats())


@sos_bp.route("/sos/<int:sos_id>", methods=["PUT"])
def update_status(sos_id):

    data = request.get_json()

    update_sos_status(
        sos_id,
        data["status"]
    )

    return jsonify({
        "message": "Status Updated Successfully"
    })


@sos_bp.route("/sos/<int:sos_id>", methods=["DELETE"])
def remove_sos(sos_id):

    delete_sos(sos_id)

    return jsonify({
        "message": "SOS Request Deleted Successfully"
    })