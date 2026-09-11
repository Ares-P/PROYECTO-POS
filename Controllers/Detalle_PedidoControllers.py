from flask import jsonify, request
from Services.Detalle_PedidoServices import Detalle_PedidoServices


class Detalle_PedidoControllers:

    def consult():
        data = Detalle_PedidoServices.consult()
        return jsonify({"Mensaje": "Listado de detalles de pedido", "data": data}), 200

    def create():
        body_data = request.get_json()
        result = Detalle_PedidoServices.add(body_data)
        return jsonify({"Mensaje": "Detalle de pedido creado correctamente", "data": result}), 201

    def update(uuid):
        body_data = request.get_json(silent=True)
        if not body_data:
            return jsonify({"Mensaje": "el cuerpo esta vacio o invalido"}), 400

        result = Detalle_PedidoServices.update(uuid, body_data)
        if result == 404:
            return jsonify({"Mensaje": "no se encontro detalle de pedido"}), 404
        return jsonify({"mensaje": "Detalle de pedido actualizado correctamente", "data": result}), 200

    def delete(uuid):
        x = Detalle_PedidoServices.delete(uuid)
        if x == 404:
            return jsonify({"Mensaje": "no se encontro detalle de pedido"}), x
        else:
            return jsonify({"mensaje": "Detalle de pedido eliminado correctamente"}), x
