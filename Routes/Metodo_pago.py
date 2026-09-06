from flask import Blueprint
from Controllers.Metodo_pagoControllers import Metodo_pagoControllers

metodo_pago_bp = Blueprint("Metodo_pago", __name__)


@metodo_pago_bp.route("/", methods=["GET"])
def consult():
    return Metodo_pagoControllers.consult()


@metodo_pago_bp.route("/", methods=["POST"])
def add():
    return Metodo_pagoControllers.create()


@metodo_pago_bp.route("/<int:id>", methods=["PUT"])
def update(id):
    return Metodo_pagoControllers.update(id)


@metodo_pago_bp.route("/<int:id>", methods=["DELETE"])
def delete(id):
    return Metodo_pagoControllers.delete(id)
