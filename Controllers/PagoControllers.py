from flask import jsonify, request
from Services.PagoServices import PagoServices


class PagoControllers:

    def consult():
        data = PagoServices.consult()
        return jsonify({"Mensaje": "Listado de pagos", "data": data}), 200

    def create():
        body_data = request.get_json()
        result = PagoServices.add(body_data)
        return jsonify({"Mensaje": "Pago creado correctamente", "data": result}), 201

    def update(uuid):
        body_data = request.get_json(silent=True)
        if not body_data:
            return jsonify({"Mensaje": "el cuerpo esta vacio o invalido"}), 400

        result = PagoServices.update(uuid, body_data)
        if result == 404:
            return jsonify({"Mensaje": "no se encontro pago"}), 404
        return jsonify({"mensaje": "Pago actualizado correctamente", "data": result}), 200

    def delete(uuid):
        x = PagoServices.delete(uuid)
        if x == 404:
            return jsonify({"Mensaje": "no se encontro pago"}), x
        else:
            return jsonify({"mensaje": "Pago eliminado correctamente"}), x
