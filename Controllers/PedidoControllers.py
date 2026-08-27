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

    def update(id):
        body_data = request.get_json()
        result = PedidoServices.update(id, body_data)
        return jsonify({"Mensaje": "Pedido actualizado correctamente", "data": result}), 200

    def delete(id):
        result = PedidoServices.delete(id)
        return jsonify({"Mensaje": "Pedido eliminado correctamente", "data": result}), 200
