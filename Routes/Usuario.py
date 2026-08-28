from flask import Blueprint, request, jsonify
from Services.UsuarioServices import UsuarioServices

usuario_bp = Blueprint("Usuario", __name__)


@usuario_bp.route("/", methods=["GET"])
def consult():
    data = UsuarioServices.consult()
    return data


@usuario_bp.route("/", methods=["POST"])
def add():
    data = request.get_json()
    result = UsuarioServices.add(data)
    return result


@usuario_bp.route("/<int:id>", methods=["PUT"])
def update(id):
    data = request.get_json()
    result = UsuarioServices.update(id, data)
    return jsonify(result)


@usuario_bp.route("/<int:id>", methods=["DELETE"])
def delete(id):
    result = UsuarioServices.delete(id)
    return jsonify(result)
