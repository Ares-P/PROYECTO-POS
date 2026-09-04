from flask import Blueprint
from Controllers.Estado_PedidoControllers import Estado_PedidoControllers

estado_pedido_bp = Blueprint("Estado_Pedido", __name__)


@estado_pedido_bp.route("/", methods=["GET"])
def consult():
    return Estado_PedidoControllers.consult()


@estado_pedido_bp.route("/", methods=["POST"])
def add():
    return Estado_PedidoControllers.create()


@estado_pedido_bp.route("/<int:id>", methods=["PUT"])
def update(id):
    return Estado_PedidoControllers.update(id)


@estado_pedido_bp.route("/<int:id>", methods=["DELETE"])
def delete(id):
    return Estado_PedidoControllers.delete(id)
