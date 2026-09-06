from flask import Blueprint
from Controllers.RolControllers import RolControllers

rol_bp = Blueprint("Rol", __name__)


@rol_bp.route("/", methods=["GET"])
def consult():
    return RolControllers.consult()


@rol_bp.route("/", methods=["POST"])
def add():
    return RolControllers.add()


@rol_bp.route("/<int:id>", methods=["PUT"])
def update(id):
    return RolControllers.update(id)


@rol_bp.route("/<int:id>", methods=["DELETE"])
def delete(id):
    return RolControllers.delete(id)
