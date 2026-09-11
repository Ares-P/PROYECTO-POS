from flask import Blueprint
from Controllers.CategoriaControllers import CategoriaControllers

categoria_bp = Blueprint("Categoria", __name__)


@categoria_bp.route("/", methods=["GET"])
def consult():
    return CategoriaControllers.consult()


@categoria_bp.route("/", methods=["POST"])
def add():
    return CategoriaControllers.create()


@categoria_bp.route("/<uuid>", methods=["PUT"])
def update(uuid):
    return CategoriaControllers.update(uuid)


@categoria_bp.route("/<uuid>", methods=["DELETE"])
def delete(uuid):
    return CategoriaControllers.delete(uuid)
