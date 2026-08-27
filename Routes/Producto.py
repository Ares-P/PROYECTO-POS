from flask import Blueprint, request, jsonify
from Services.ProductoServices import ProductoServices

producto_bp = Blueprint("Producto", __name__)


@producto_bp.route("/", methods=["GET"])
def consult():
    data = ProductoServices.consult()
    return jsonify(data)


@producto_bp.route("/", methods=["POST"])
def add():
    data = request.get_json()
    result = ProductoServices.add(data)
    return jsonify(result)


@producto_bp.route("/<int:id>", methods=["PUT"])
def update(id):
    data = request.get_json()
    result = ProductoServices.update(id, data)
    return jsonify(result)


@producto_bp.route("/<int:id>", methods=["DELETE"])
def delete(id):
    result = ProductoServices.delete(id)
    return jsonify(result)
