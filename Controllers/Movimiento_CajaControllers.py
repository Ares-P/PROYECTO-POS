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

    def update(uuid):
        body_data = request.get_json(silent=True)
        if not body_data:
            return jsonify({"Mensaje": "el cuerpo esta vacio o invalido"}), 400

        result = Movimiento_CajaServices.update(uuid, body_data)
        if result == 404:
            return jsonify({"Mensaje": "no se encontro movimiento de caja"}), 404
        return jsonify({"mensaje": "Movimiento de caja actualizado correctamente", "data": result}), 200

    def delete(uuid):
        x = Movimiento_CajaServices.delete(uuid)
        if x == 404:
            return jsonify({"Mensaje": "no se encontro movimiento de caja"}), x
        else:
            return jsonify({"mensaje": "Movimiento de caja eliminado correctamente"}), x
