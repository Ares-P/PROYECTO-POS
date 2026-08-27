from flask import jsonify, request
from Services.Movimiento_CajaServices import Movimiento_CajaServices


class Movimiento_CajaControllers:

    def consult():
        data = Movimiento_CajaServices.consult()
        return jsonify({"Mensaje": "Listado de movimientos de caja", "data": data}), 200

    def create():
        body_data = request.get_json()
        result = Movimiento_CajaServices.add(body_data)
        return jsonify({"Mensaje": "Movimiento de caja creado correctamente", "data": result}), 201

    def update(id):
        body_data = request.get_json()
        result = Movimiento_CajaServices.update(id, body_data)
        return jsonify({"Mensaje": "Movimiento de caja actualizado correctamente", "data": result}), 200

    def delete(id):
        result = Movimiento_CajaServices.delete(id)
        return jsonify({"Mensaje": "Movimiento de caja eliminado correctamente", "data": result}), 200
