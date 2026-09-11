from flask import Blueprint
from Controllers.RolControllers import RolControllers

rol_bp = Blueprint("Rol", __name__)


@rol_bp.route("/", methods=["GET"])
def consult():
    return RolControllers.consult()


@rol_bp.route("/", methods=["POST"])
def add():
    return RolControllers.add()


@rol_bp.route("/<uuid>", methods=["PUT"])
def update(uuid):
    return RolControllers.update(uuid)


@rol_bp.route("/<uuid>", methods=["DELETE"])
def delete(uuid):
    return RolControllers.delete(uuid)
