from flask import Blueprint
from Controllers.PagoControllers import PagoControllers

pago_bp = Blueprint("Pago", __name__)


@pago_bp.route("/", methods=["GET"])
def consult():
    return PagoControllers.consult()


@pago_bp.route("/", methods=["POST"])
def add():
    return PagoControllers.create()


@pago_bp.route("/<int:id>", methods=["PUT"])
def update(id):
    return PagoControllers.update(id)


@pago_bp.route("/<int:id>", methods=["DELETE"])
def delete(id):
    return PagoControllers.delete(id)
