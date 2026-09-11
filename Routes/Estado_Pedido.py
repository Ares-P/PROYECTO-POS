from flask import Blueprint
from Controllers.Estado_PedidoControllers import Estado_PedidoControllers

estado_pedido_bp = Blueprint("Estado_Pedido", __name__)


@estado_pedido_bp.route("/", methods=["GET"])
def consult():
    return Estado_PedidoControllers.consult()


@estado_pedido_bp.route("/", methods=["POST"])
def add():
    return Estado_PedidoControllers.create()


@estado_pedido_bp.route("/<uuid>", methods=["PUT"])
def update(uuid):
    return Estado_PedidoControllers.update(uuid)


@estado_pedido_bp.route("/<uuid>", methods=["DELETE"])
def delete(uuid):
    return Estado_PedidoControllers.delete(uuid)
