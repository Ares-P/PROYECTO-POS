from flask import jsonify, request
from Services.ProductoServices import ProductoServices


class ProductoControllers:

    def consult():
        data = ProductoServices.consult()
        return jsonify({"Mensaje": "Listado de productos", "data": data}), 200

    def create():
        body_data = request.get_json()
        result = ProductoServices.add(body_data)
        return jsonify({"Mensaje": "Producto creado correctamente", "data": result}), 201

    def update(uuid):
        body_data = request.get_json(silent=True)
        if not body_data:
            return jsonify({"Mensaje": "el cuerpo esta vacio o invalido"}), 400

        result = ProductoServices.update(uuid, body_data)
        if result == 404:
            return jsonify({"Mensaje": "no se encontro producto"}), 404
        return jsonify({"mensaje": "Producto actualizado correctamente", "data": result}), 200

    def delete(uuid):
        x = ProductoServices.delete(uuid)
        if x == 404:
            return jsonify({"Mensaje": "no se encontro producto"}), x
        else:
            return jsonify({"mensaje": "Producto eliminado correctamente"}), x
