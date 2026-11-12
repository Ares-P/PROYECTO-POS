from flask import jsonify, request
from Services.PagoServices import PagoServices


class PagoControllers:

    def consult():
        data = PagoServices.consult()
        return jsonify({"mensaje": data}), 200

    def create():
        data = request.get_json(silent=True)
        if not data or not isinstance(data, dict):
            return jsonify({"mensaje": "El cuerpo está vacío o no contiene un JSON válido"}), 400

        requeridos = ['id_pago', 'referencia', 'estado', 'fecha_pago', 'valor_pagado', 'ped_id', 'met_pag_id', 'caj_id']
        falta = [campo for campo in requeridos if campo not in data or data[campo] is None or (isinstance(data[campo], str) and not data[campo].strip())]
        if falta:
            return jsonify({"mensaje": f"Faltan parámetros obligatorios: {falta}"}), 400

        resultado = PagoServices.add(data)
        return jsonify({"mensaje": "Pago creado correctamente", "data": resultado}), 201

    def update(uuid):
        body_data = request.get_json(silent=True)
        if not body_data or not isinstance(body_data, dict):
            return jsonify({"mensaje": "El cuerpo está vacío o no contiene un JSON válido"}), 400

        requeridos = ['id_pago', 'referencia', 'estado', 'fecha_pago', 'valor_pagado', 'ped_id', 'met_pag_id', 'caj_id']
        falta = [campo for campo in requeridos if campo not in body_data or body_data[campo] is None or (isinstance(body_data[campo], str) and not body_data[campo].strip())]
        if falta:
            return jsonify({"mensaje": f"Faltan parámetros obligatorios: {falta}"}), 400

        resultado = PagoServices.update(uuid, body_data)
        if resultado == 404:
            return jsonify({"mensaje": "No se encontró pago"}), 404
        return jsonify({"mensaje": "Pago actualizado correctamente", "data": resultado}), 200

    def delete(uuid):
        resultado = PagoServices.delete(uuid)
        if resultado == 404:
            return jsonify({"mensaje": "No se encontró pago"}), 404
        return jsonify({"mensaje": "Pago eliminado correctamente"}), 200
