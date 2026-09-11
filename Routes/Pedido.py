from flask import Blueprint
from Controllers.PedidoControllers import PedidoControllers

pedido_bp = Blueprint("Pedido", __name__)


@pedido_bp.route("/", methods=["GET"])
def consult():
    return PedidoControllers.consult()


@pedido_bp.route("/", methods=["POST"])
def add():
    return PedidoControllers.create()


@pedido_bp.route("/<uuid>", methods=["PUT"])
def update(uuid):
    return PedidoControllers.update(uuid)


@pedido_bp.route("/<uuid>", methods=["DELETE"])
def delete(uuid):
    return PedidoControllers.delete(uuid)
