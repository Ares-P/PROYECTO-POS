from flask import Blueprint
from Controllers.Detalle_PedidoControllers import Detalle_PedidoControllers

detalle_pedido_bp = Blueprint("Detalle_Pedido", __name__)


@detalle_pedido_bp.route("/", methods=["GET"])
def consult():
    return Detalle_PedidoControllers.consult()


@detalle_pedido_bp.route("/", methods=["POST"])
def add():
    return Detalle_PedidoControllers.create()


@detalle_pedido_bp.route("/<int:id>", methods=["PUT"])
def update(id):
    return Detalle_PedidoControllers.update(id)


@detalle_pedido_bp.route("/<int:id>", methods=["DELETE"])
def delete(id):
    return Detalle_PedidoControllers.delete(id)
