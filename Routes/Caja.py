from flask import Blueprint
from Controllers.CajaControllers import CajaControllers

caja_bp = Blueprint("Caja", __name__)


@caja_bp.route("/", methods=["GET"])
def consult():
    return CajaControllers.consult()


@caja_bp.route("/", methods=["POST"])
def add():
    return CajaControllers.create()


@caja_bp.route("/<uuid>", methods=["PUT"])
def update(uuid):
    return CajaControllers.update(uuid)


@caja_bp.route("/<uuid>", methods=["DELETE"])
def delete(uuid):
    return CajaControllers.delete(uuid)
