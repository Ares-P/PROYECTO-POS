from flask import Blueprint
from Controllers.UsuarioControllers import UsuarioControllers

usuario_bp = Blueprint("Usuario", __name__)


@usuario_bp.route("/", methods=["GET"])
def consult():
    return UsuarioControllers.consult()


@usuario_bp.route("/", methods=["POST"])
def add():
    return UsuarioControllers.create()


@usuario_bp.route("/<uuid>", methods=["PUT"])
def update(uuid):
    return UsuarioControllers.update(uuid)


@usuario_bp.route("/<uuid>", methods=["DELETE"])
def delete(uuid):
    return UsuarioControllers.delete(uuid)
