from flask import Blueprint
from Controllers.Movimiento_CajaControllers import Movimiento_CajaControllers

movimiento_caja_bp = Blueprint("Movimiento_Caja", __name__)


@movimiento_caja_bp.route("/", methods=["GET"])
def consult():
    return Movimiento_CajaControllers.consult()


@movimiento_caja_bp.route("/", methods=["POST"])
def add():
    return Movimiento_CajaControllers.create()


@movimiento_caja_bp.route("/<uuid>", methods=["PUT"])
def update(uuid):
    return Movimiento_CajaControllers.update(uuid)


@movimiento_caja_bp.route("/<uuid>", methods=["DELETE"])
def delete(uuid):
    return Movimiento_CajaControllers.delete(uuid)
