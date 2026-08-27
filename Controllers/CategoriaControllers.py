from flask import jsonify, request
from Services.CategoriaServices import CategoriaServices


class CategoriaControllers:

    def consult():
        data = CategoriaServices.consult()
        return jsonify({"Mensaje": "Listado de categorías", "data": data}), 200

    def create():
        body_data = request.get_json()
        result = CategoriaServices.add(body_data)
        return jsonify({"Mensaje": "Categoría creada correctamente", "data": result}), 201

    def update(id):
        body_data = request.get_json()
        result = CategoriaServices.update(id, body_data)
        return jsonify({"Mensaje": "Categoría actualizada correctamente", "data": result}), 200

    def delete(id):
        result = CategoriaServices.delete(id)
        return jsonify({"Mensaje": "Categoría eliminada correctamente", "data": result}), 200
