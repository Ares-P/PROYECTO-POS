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

    def update(uuid):
        body_data = request.get_json(silent=True)
        if not body_data:
            return jsonify({"Mensaje": "el cuerpo esta vacio o invalido"}), 400

        result = MesaServices.update(uuid, body_data)
        if result == 404:
            return jsonify({"Mensaje": "no se encontro mesa"}), 404
        return jsonify({"mensaje": "Mesa actualizado correctamente", "data": result}), 200

    def delete(uuid):
        x = MesaServices.delete(uuid)
        if x == 404:
            return jsonify({"Mensaje": "no se encontro mesa"}), x
        else:
            return jsonify({"mensaje": "Mesa eliminado correctamente"}), x
