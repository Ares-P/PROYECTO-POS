from flask import Blueprint, request, jsonify
from Services.Metodo_pagoServices import Metodo_pagoServices

metodo_pago_bp = Blueprint("Metodo_pago", __name__)


@metodo_pago_bp.route("/", methods=["GET"])
def consult():
    data = Metodo_pagoServices.consult()
    return jsonify(data)


@metodo_pago_bp.route("/", methods=["POST"])
def add():
    data = request.get_json()
    result = Metodo_pagoServices.add(data)
    return jsonify(result)


@metodo_pago_bp.route("/<int:id>", methods=["PUT"])
def update(id):
    data = request.get_json()
    result = Metodo_pagoServices.update(id, data)
    return jsonify(result)


@metodo_pago_bp.route("/<int:id>", methods=["DELETE"])
def delete(id):
    result = Metodo_pagoServices.delete(id)
    return jsonify(result)
