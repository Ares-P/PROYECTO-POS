from flask import Blueprint, request, jsonify
from Controllers.CajaControllers import CajaControllers

caja_bp = Blueprint("Caja", __name__)


@caja_bp.route("/", methods=["GET"])
def consult():
    data = CajaControllers.consult()
    return jsonify(data)


@caja_bp.route("/", methods=["POST"])
def add():
    data = request.get_json()
    result = CajaControllers.add(data)
    return jsonify(result)


@caja_bp.route("/<int:id>", methods=["PUT"])
def update(id):
    data = request.get_json()
    result = CajaControllers.update(id, data)
    return jsonify(result)


@caja_bp.route("/<int:id>", methods=["DELETE"])
def delete(id):
    result = CajaControllers.delete(id)
    return jsonify(result)
