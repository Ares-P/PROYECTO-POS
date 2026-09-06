from flask import Blueprint
from Controllers.MesaControllers import MesaControllers

mesa_bp = Blueprint("Mesa", __name__)


@mesa_bp.route("/", methods=["GET"])
def consult():
    return MesaControllers.consult()


@mesa_bp.route("/", methods=["POST"])
def add():
    return MesaControllers.create()


@mesa_bp.route("/<int:id>", methods=["PUT"])
def update(id):
    return MesaControllers.update(id)


@mesa_bp.route("/<int:id>", methods=["DELETE"])
def delete(id):
    return MesaControllers.delete(id)
