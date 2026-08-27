from flask import Blueprint, request, jsonify
from Services.Estado_PedidoServices import Estado_PedidoServices

estado_pedido_bp = Blueprint("Estado_Pedido", __name__)


@estado_pedido_bp.route("/", methods=["GET"])
def consult():
    data = Estado_PedidoServices.consult()
    return jsonify(data)


@estado_pedido_bp.route("/", methods=["POST"])
def add():
    data = request.get_json()
    result = Estado_PedidoServices.add(data)
    return jsonify(result)


@estado_pedido_bp.route("/<int:id>", methods=["PUT"])
def update(id):
    data = request.get_json()
    result = Estado_PedidoServices.update(id, data)
    return jsonify(result)


@estado_pedido_bp.route("/<int:id>", methods=["DELETE"])
def delete(id):
    result = Estado_PedidoServices.delete(id)
    return jsonify(result)
