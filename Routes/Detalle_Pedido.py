from flask import Blueprint
from Controllers.Detalle_PedidoControllers import Detalle_PedidoControllers

detalle_pedido_bp = Blueprint("Detalle_Pedido", __name__)


@detalle_pedido_bp.route("/", methods=["GET"])
def consult():
    return Detalle_PedidoControllers.consult()


@detalle_pedido_bp.route("/", methods=["POST"])
def add():
    return Detalle_PedidoControllers.create()


@detalle_pedido_bp.route("/<uuid>", methods=["PUT"])
def update(uuid):
    return Detalle_PedidoControllers.update(uuid)


@detalle_pedido_bp.route("/<uuid>", methods=["DELETE"])
def delete(uuid):
    return Detalle_PedidoControllers.delete(uuid)
