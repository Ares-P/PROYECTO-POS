from flask import Blueprint, request, jsonify
from Services.CategoriaServices import CategoriaServices

categoria_bp = Blueprint("Categoria", __name__)


@categoria_bp.route("/", methods=["GET"])
def consult():
    data = CategoriaServices.consult()
    return jsonify(data)


@categoria_bp.route("/", methods=["POST"])
def add():
    data = request.get_json()
    result = CategoriaServices.add(data)
    return jsonify(result)


@categoria_bp.route("/<int:id>", methods=["PUT"])
def update(id):
    data = request.get_json()
    result = CategoriaServices.update(id, data)
    return jsonify(result)


@categoria_bp.route("/<int:id>", methods=["DELETE"])
def delete(id):
    result = CategoriaServices.delete(id)
    return jsonify(result)
