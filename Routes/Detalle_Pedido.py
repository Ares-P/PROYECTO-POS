from flask import Blueprint, request, jsonify
from Services.Detalle_PedidoServices import Detalle_PedidoServices

detalle_pedido_bp = Blueprint("Detalle_Pedido", __name__)


@detalle_pedido_bp.route("/", methods=["GET"])
def consult():
    data = Detalle_PedidoServices.consult()
    return jsonify(data)


@detalle_pedido_bp.route("/", methods=["POST"])
def add():
    data = request.get_json()
    result = Detalle_PedidoServices.add(data)
    return jsonify(result)


@detalle_pedido_bp.route("/<int:id>", methods=["PUT"])
def update(id):
    data = request.get_json()
    result = Detalle_PedidoServices.update(id, data)
    return jsonify(result)


@detalle_pedido_bp.route("/<int:id>", methods=["DELETE"])
def delete(id):
    result = Detalle_PedidoServices.delete(id)
    return jsonify(result)
