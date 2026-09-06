from flask import Blueprint
from Controllers.PedidoControllers import PedidoControllers

pedido_bp = Blueprint("Pedido", __name__)


@pedido_bp.route("/", methods=["GET"])
def consult():
    return PedidoControllers.consult()


@pedido_bp.route("/", methods=["POST"])
def add():
    return PedidoControllers.create()


@pedido_bp.route("/<int:id>", methods=["PUT"])
def update(id):
    return PedidoControllers.update(id)


@pedido_bp.route("/<int:id>", methods=["DELETE"])
def delete(id):
    return PedidoControllers.delete(id)
