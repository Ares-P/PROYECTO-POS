from flask import Blueprint, request, jsonify
from Services.PagoServices import PagoServices

pago_bp = Blueprint("Pago", __name__)


@pago_bp.route("/", methods=["GET"])
def consult():
    data = PagoServices.consult()
    return jsonify(data)


@pago_bp.route("/", methods=["POST"])
def add():
    data = request.get_json()
    result = PagoServices.add(data)
    return jsonify(result)


@pago_bp.route("/<int:id>", methods=["PUT"])
def update(id):
    data = request.get_json()
    result = PagoServices.update(id, data)
    return jsonify(result)


@pago_bp.route("/<int:id>", methods=["DELETE"])
def delete(id):
    result = PagoServices.delete(id)
    return jsonify(result)
