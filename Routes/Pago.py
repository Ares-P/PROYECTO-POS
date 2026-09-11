from flask import Blueprint
from Controllers.PagoControllers import PagoControllers

pago_bp = Blueprint("Pago", __name__)


@pago_bp.route("/", methods=["GET"])
def consult():
    return PagoControllers.consult()


@pago_bp.route("/", methods=["POST"])
def add():
    return PagoControllers.create()


@pago_bp.route("/<uuid>", methods=["PUT"])
def update(uuid):
    return PagoControllers.update(uuid)


@pago_bp.route("/<uuid>", methods=["DELETE"])
def delete(uuid):
    return PagoControllers.delete(uuid)
