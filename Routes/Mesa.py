from flask import Blueprint
from Controllers.MesaControllers import MesaControllers

mesa_bp = Blueprint("Mesa", __name__)


@mesa_bp.route("/", methods=["GET"])
def consult():
    return MesaControllers.consult()


@mesa_bp.route("/", methods=["POST"])
def add():
    return MesaControllers.create()


@mesa_bp.route("/<uuid>", methods=["PUT"])
def update(uuid):
    return MesaControllers.update(uuid)


@mesa_bp.route("/<uuid>", methods=["DELETE"])
def delete(uuid):
    return MesaControllers.delete(uuid)
