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

    def update(id):
        body_data = request.get_json()
        result = CajaServices.update(id, body_data)
        return jsonify({"Mensaje": "Caja actualizada correctamente", "data": result}), 200

    def delete(id):
        result = CajaServices.delete(id)
        return jsonify({"Mensaje": "Caja eliminada correctamente", "data": result}), 200
