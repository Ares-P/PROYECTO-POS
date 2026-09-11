from flask import jsonify, request
from Services.CajaServices import CajaServices


class CajaControllers:

    def consult():
        data = CajaServices.consult()
        return jsonify({"mensaje":data}), 200

    def create():
        body_data = request.get_json()
        result = CajaServices.add(body_data)
        return jsonify({"Mensaje": "Caja actualizada correctamente", "data": result}), 200

    def update(uuid):
        body_data = request.get_json(silent=True)
        if not body_data:
            return jsonify({"Mensaje": "el cuerpo esta vacio o invalido"}), 400

        result = CajaServices.update(uuid, body_data)
        if result == 404:
            return jsonify({"Mensaje": "no se encontro caja"}), 404
        return jsonify({"mensaje": "Caja actualizado correctamente", "data": result}), 200

    def delete(uuid):
        x = CajaServices.delete(uuid)
        if x == 404:
            return jsonify({"Mensaje": "no se encontro caja"}), x
        else:
            return jsonify({"mensaje": "Caja eliminado correctamente"}), x
