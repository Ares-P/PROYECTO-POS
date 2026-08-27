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

    def update(id):
        body_data = request.get_json()
        result = Detalle_PedidoServices.update(id, body_data)
        return jsonify({"Mensaje": "Detalle de pedido actualizado correctamente", "data": result}), 200

    def delete(id):
        result = Detalle_PedidoServices.delete(id)
        return jsonify({"Mensaje": "Detalle de pedido eliminado correctamente", "data": result}), 200
