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

    def update(id):
        body_data = request.get_json()
        result = Metodo_pagoServices.update(id, body_data)
        return jsonify({"Mensaje": "Método de pago actualizado correctamente", "data": result}), 200

    def delete(id):
        result = Metodo_pagoServices.delete(id)
        return jsonify({"Mensaje": "Método de pago eliminado correctamente", "data": result}), 200
