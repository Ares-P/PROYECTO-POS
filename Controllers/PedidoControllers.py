from flask import jsonify, request
from Services.PedidoServices import PedidoServices


class PedidoControllers:

    def consult():
        data = PedidoServices.consult()
        return jsonify({"Mensaje": "Listado de pedidos", "data": data}), 200

    def create():
        body_data = request.get_json()
        result = PedidoServices.add(body_data)
        return jsonify({"Mensaje": "Pedido creado correctamente", "data": result}), 201

    def update(uuid):
        body_data = request.get_json(silent=True)
        if not body_data:
            return jsonify({"Mensaje": "el cuerpo esta vacio o invalido"}), 400

        result = PedidoServices.update(uuid, body_data)
        if result == 404:
            return jsonify({"Mensaje": "no se encontro pedido"}), 404
        return jsonify({"mensaje": "Pedido actualizado correctamente", "data": result}), 200

    def delete(uuid):
        x = PedidoServices.delete(uuid)
        if x == 404:
            return jsonify({"Mensaje": "no se encontro pedido"}), x
        else:
            return jsonify({"mensaje": "Pedido eliminado correctamente"}), x
