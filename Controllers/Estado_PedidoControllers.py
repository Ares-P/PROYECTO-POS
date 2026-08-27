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

    def update(id):
        body_data = request.get_json()
        result = Estado_PedidoServices.update(id, body_data)
        return jsonify({"Mensaje": "Estado de pedido actualizado correctamente", "data": result}), 200

    def delete(id):
        result = Estado_PedidoServices.delete(id)
        return jsonify({"Mensaje": "Estado de pedido eliminado correctamente", "data": result}), 200
