from flask import Blueprint
from Controllers.Metodo_pagoControllers import Metodo_pagoControllers

metodo_pago_bp = Blueprint("Metodo_pago", __name__)


@metodo_pago_bp.route("/", methods=["GET"])
def consult():
    return Metodo_pagoControllers.consult()


@metodo_pago_bp.route("/", methods=["POST"])
def add():
    return Metodo_pagoControllers.create()


@metodo_pago_bp.route("/<uuid>", methods=["PUT"])
def update(uuid):
    return Metodo_pagoControllers.update(uuid)


@metodo_pago_bp.route("/<uuid>", methods=["DELETE"])
def delete(uuid):
    return Metodo_pagoControllers.delete(uuid)
