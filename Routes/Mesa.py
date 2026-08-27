from flask import Blueprint, request, jsonify
from Services.MesaServices import MesaServices

mesa_bp = Blueprint("Mesa", __name__)


@mesa_bp.route("/", methods=["GET"])
def consult():
    data = MesaServices.consult()
    return jsonify(data)


@mesa_bp.route("/", methods=["POST"])
def add():
    data = request.get_json()
    result = MesaServices.add(data)
    return jsonify(result)


@mesa_bp.route("/<int:id>", methods=["PUT"])
def update(id):
    data = request.get_json()
    result = MesaServices.update(id, data)
    return jsonify(result)


@mesa_bp.route("/<int:id>", methods=["DELETE"])
def delete(id):
    result = MesaServices.delete(id)
    return jsonify(result)
