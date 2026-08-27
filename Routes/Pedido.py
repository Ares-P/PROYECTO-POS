from flask import Blueprint, request, jsonify
from Services.PedidoServices import PedidoServices

pedido_bp = Blueprint("Pedido", __name__)


@pedido_bp.route("/", methods=["GET"])
def consult():
    data = PedidoServices.consult()
    return jsonify(data)


@pedido_bp.route("/", methods=["POST"])
def add():
    data = request.get_json()
    result = PedidoServices.add(data)
    return jsonify(result)


@pedido_bp.route("/<int:id>", methods=["PUT"])
def update(id):
    data = request.get_json()
    result = PedidoServices.update(id, data)
    return jsonify(result)


@pedido_bp.route("/<int:id>", methods=["DELETE"])
def delete(id):
    result = PedidoServices.delete(id)
    return jsonify(result)
