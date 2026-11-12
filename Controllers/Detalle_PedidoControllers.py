from flask import jsonify, request
from Services.Detalle_PedidoServices import Detalle_PedidoServices


class Detalle_PedidoControllers:

    def consult():
        data = Detalle_PedidoServices.consult()
        return jsonify({"mensaje": data}), 200

    def create():
        data = request.get_json(silent=True)
        if not data or not isinstance(data, dict):
            return jsonify({"mensaje": "El cuerpo está vacío o no contiene un JSON válido"}), 400

        requeridos = ['cantidad', 'precio_unitario', 'subtotal', 'ped_id', 'pro_id']
        falta = [campo for campo in requeridos if campo not in data or data[campo] is None or (isinstance(data[campo], str) and not data[campo].strip())]
        if falta:
            return jsonify({"mensaje": f"Faltan parámetros obligatorios: {falta}"}), 400

        resultado = Detalle_PedidoServices.add(data)
        return jsonify({"mensaje": "Detalle de pedido creado correctamente", "data": resultado}), 201

    def update(uuid):
        body_data = request.get_json(silent=True)
        if not body_data or not isinstance(body_data, dict):
            return jsonify({"mensaje": "El cuerpo está vacío o no contiene un JSON válido"}), 400

        requeridos = ['cantidad', 'precio_unitario', 'subtotal', 'ped_id', 'pro_id']
        falta = [campo for campo in requeridos if campo not in body_data or body_data[campo] is None or (isinstance(body_data[campo], str) and not body_data[campo].strip())]
        if falta:
            return jsonify({"mensaje": f"Faltan parámetros obligatorios: {falta}"}), 400

        resultado = Detalle_PedidoServices.update(uuid, body_data)
        if resultado == 404:
            return jsonify({"mensaje": "No se encontró detalle de pedido"}), 404
        return jsonify({"mensaje": "Detalle de pedido actualizado correctamente", "data": resultado}), 200

    def delete(uuid):
        resultado = Detalle_PedidoServices.delete(uuid)
        if resultado == 404:
            return jsonify({"mensaje": "No se encontró detalle de pedido"}), 404
        return jsonify({"mensaje": "Detalle de pedido eliminado correctamente"}), 200
