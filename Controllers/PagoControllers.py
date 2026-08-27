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

    def update(id):
        body_data = request.get_json()
        result = PagoServices.update(id, body_data)
        return jsonify({"Mensaje": "Pago actualizado correctamente", "data": result}), 200

    def delete(id):
        result = PagoServices.delete(id)
        return jsonify({"Mensaje": "Pago eliminado correctamente", "data": result}), 200
