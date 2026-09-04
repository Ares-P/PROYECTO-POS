from flask import Blueprint
from Controllers.Movimiento_CajaControllers import Movimiento_CajaControllers

movimiento_caja_bp = Blueprint("Movimiento_Caja", __name__)


@movimiento_caja_bp.route("/", methods=["GET"])
def consult():
    return Movimiento_CajaControllers.consult()


@movimiento_caja_bp.route("/", methods=["POST"])
def add():
    return Movimiento_CajaControllers.create()


@movimiento_caja_bp.route("/<int:id>", methods=["PUT"])
def update(id):
    return Movimiento_CajaControllers.update(id)


@movimiento_caja_bp.route("/<int:id>", methods=["DELETE"])
def delete(id):
    return Movimiento_CajaControllers.delete(id)
