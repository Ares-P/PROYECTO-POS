from flask import Blueprint, request, jsonify
from Controllers.RolControllers import RolControllers

rol_bp = Blueprint("Rol", __name__)


@rol_bp.route("/", methods=["GET"])
def consult():
    data = RolControllers.consult()
    return data


@rol_bp.route("/", methods=["POST"])
def add():
    result = RolControllers.add()
    return result


@rol_bp.route("/<int:id>", methods=["PUT"])
def update(id):
    data = request.get_json()
    result = RolControllers.update(id, data)
    return jsonify(result)


@rol_bp.route("/<int:id>", methods=["DELETE"])
def delete(id):
    result = RolControllers.delete(id)
    return jsonify(result)
