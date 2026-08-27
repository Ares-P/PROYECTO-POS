from flask import jsonify, request
from Services.MesaServices import MesaServices


class MesaControllers:

    def consult():
        data = MesaServices.consult()
        return jsonify({"Mensaje": "Listado de mesas", "data": data}), 200

    def create():
        body_data = request.get_json()
        result = MesaServices.add(body_data)
        return jsonify({"Mensaje": "Mesa creada correctamente", "data": result}), 201

    def update(id):
        body_data = request.get_json()
        result = MesaServices.update(id, body_data)
        return jsonify({"Mensaje": "Mesa actualizada correctamente", "data": result}), 200

    def delete(id):
        result = MesaServices.delete(id)
        return jsonify({"Mensaje": "Mesa eliminada correctamente", "data": result}), 200
