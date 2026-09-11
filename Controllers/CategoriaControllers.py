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

    def update(uuid):
        body_data = request.get_json(silent=True)
        if not body_data:
            return jsonify({"Mensaje": "el cuerpo esta vacio o invalido"}), 400

        result = CategoriaServices.update(uuid, body_data)
        if result == 404:
            return jsonify({"Mensaje": "no se encontro categoría"}), 404
        return jsonify({"mensaje": "Categoría actualizado correctamente", "data": result}), 200

    def delete(uuid):
        x = CategoriaServices.delete(uuid)
        if x == 404:
            return jsonify({"Mensaje": "no se encontro categoría"}), x
        else:
            return jsonify({"mensaje": "Categoría eliminado correctamente"}), x
