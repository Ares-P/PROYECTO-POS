from flask import Blueprint, request, jsonify
from Services.Movimiento_CajaServices import Movimiento_CajaServices

movimiento_caja_bp = Blueprint("Movimiento_Caja", __name__)


@movimiento_caja_bp.route("/", methods=["GET"])
def consult():
    data = Movimiento_CajaServices.consult()
    return jsonify(data)


@movimiento_caja_bp.route("/", methods=["POST"])
def add():
    data = request.get_json()
    result = Movimiento_CajaServices.add(data)
    return jsonify(result)


@movimiento_caja_bp.route("/<int:id>", methods=["PUT"])
def update(id):
    data = request.get_json()
    result = Movimiento_CajaServices.update(id, data)
    return jsonify(result)


@movimiento_caja_bp.route("/<int:id>", methods=["DELETE"])
def delete(id):
    result = Movimiento_CajaServices.delete(id)
    return jsonify(result)
