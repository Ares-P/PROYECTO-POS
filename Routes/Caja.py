from flask import Blueprint, request, jsonify
from Services.CajaServices import CajaServices

caja_bp = Blueprint("Caja", __name__)


@caja_bp.route("/", methods=["GET"])
def consult():
    data = CajaServices.consult()
    return jsonify(data)


@caja_bp.route("/", methods=["POST"])
def add():
    data = request.get_json()
    result = CajaServices.add(data)
    return jsonify(result)


@caja_bp.route("/<int:id>", methods=["PUT"])
def update(id):
    data = request.get_json()
    result = CajaServices.update(id, data)
    return jsonify(result)


@caja_bp.route("/<int:id>", methods=["DELETE"])
def delete(id):
    result = CajaServices.delete(id)
    return jsonify(result)
