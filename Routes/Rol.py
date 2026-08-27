from flask import Blueprint, request, jsonify
from Services.RolServices import RolServices

rol_bp = Blueprint("Rol", __name__)


@rol_bp.route("/", methods=["GET"])
def consult():
    data = RolServices.consult()
    return jsonify(data)


@rol_bp.route("/", methods=["POST"])
def add():
    data = request.get_json()
    result = RolServices.add(data)
    return jsonify(result)


@rol_bp.route("/<int:id>", methods=["PUT"])
def update(id):
    data = request.get_json()
    result = RolServices.update(id, data)
    return jsonify(result)


@rol_bp.route("/<int:id>", methods=["DELETE"])
def delete(id):
    result = RolServices.delete(id)
    return jsonify(result)
