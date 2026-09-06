from flask import Blueprint
from Controllers.CajaControllers import CajaControllers

caja_bp = Blueprint("Caja", __name__)


@caja_bp.route("/", methods=["GET"])
def consult():
    return CajaControllers.consult()


@caja_bp.route("/", methods=["POST"])
def add():
    return CajaControllers.create()


@caja_bp.route("/<int:id>", methods=["PUT"])
def update(id):
    return CajaControllers.update(id)


@caja_bp.route("/<int:id>", methods=["DELETE"])
def delete(id):
    return CajaControllers.delete(id)
