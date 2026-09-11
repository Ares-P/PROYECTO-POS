from flask import jsonify, request
from Services.Estado_PedidoServices import Estado_PedidoServices


class Estado_PedidoControllers:

    def consult():
        data = Estado_PedidoServices.consult()
        return jsonify({"Mensaje": "Listado de estados de pedido", "data": data}), 200

    def create():
        body_data = request.get_json()
        result = Estado_PedidoServices.add(body_data)
        return jsonify({"Mensaje": "Estado de pedido creado correctamente", "data": result}), 201

    def update(uuid):
        body_data = request.get_json(silent=True)
        if not body_data:
            return jsonify({"Mensaje": "el cuerpo esta vacio o invalido"}), 400

        result = Estado_PedidoServices.update(uuid, body_data)
        if result == 404:
            return jsonify({"Mensaje": "no se encontro estado de pedido"}), 404
        return jsonify({"mensaje": "Estado de pedido actualizado correctamente", "data": result}), 200

    def delete(uuid):
        x = Estado_PedidoServices.delete(uuid)
        if x == 404:
            return jsonify({"Mensaje": "no se encontro estado de pedido"}), x
        else:
            return jsonify({"mensaje": "Estado de pedido eliminado correctamente"}), x
