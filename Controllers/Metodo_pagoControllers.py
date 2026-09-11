from flask import jsonify, request
from Services.Metodo_pagoServices import Metodo_pagoServices


class Metodo_pagoControllers:

    def consult():
        data = Metodo_pagoServices.consult()
        return jsonify({"Mensaje": "Listado de métodos de pago", "data": data}), 200

    def create():
        body_data = request.get_json()
        result = Metodo_pagoServices.add(body_data)
        return jsonify({"Mensaje": "Método de pago creado correctamente", "data": result}), 201

    def update(uuid):
        body_data = request.get_json(silent=True)
        if not body_data:
            return jsonify({"Mensaje": "el cuerpo esta vacio o invalido"}), 400

        result = Metodo_pagoServices.update(uuid, body_data)
        if result == 404:
            return jsonify({"Mensaje": "no se encontro método de pago"}), 404
        return jsonify({"mensaje": "Método de pago actualizado correctamente", "data": result}), 200

    def delete(uuid):
        x = Metodo_pagoServices.delete(uuid)
        if x == 404:
            return jsonify({"Mensaje": "no se encontro método de pago"}), x
        else:
            return jsonify({"mensaje": "Método de pago eliminado correctamente"}), x
