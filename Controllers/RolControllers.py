from flask import jsonify, request
from Services.RolServices import RolServices


class RolControllers:

    def consult():
        data = RolServices.consult()
        return jsonify({"mensaje": data}), 200

    def add():
        data = request.get_json(silent=True)
        if not data or not isinstance(data, dict):
            return jsonify({"mensaje": "El cuerpo está vacío o no contiene un JSON válido"}), 400

        requeridos = ['nombre', 'descripcion']
        falta = [campo for campo in requeridos if campo not in data or data[campo] is None or (isinstance(data[campo], str) and not data[campo].strip())]
        if falta:
            return jsonify({"mensaje": f"Faltan parámetros obligatorios: {falta}"}), 400

        resultado = RolServices.add(data)
        return jsonify({"mensaje": "Se registro correctamente", "data": resultado}), 200

    def update(uuid):
        body_data = request.get_json(silent=True)
        if not body_data or not isinstance(body_data, dict):
            return jsonify({"mensaje": "El cuerpo está vacío o no contiene un JSON válido"}), 400

        requeridos = ['nombre', 'descripcion']
        falta = [campo for campo in requeridos if campo not in body_data or body_data[campo] is None or (isinstance(body_data[campo], str) and not body_data[campo].strip())]
        if falta:
            return jsonify({"mensaje": f"Faltan parámetros obligatorios: {falta}"}), 400

        resultado = RolServices.update(uuid, body_data)
        if resultado == 404:
            return jsonify({"mensaje": "No se encontró rol"}), 404
        return jsonify({"mensaje": "Rol actualizado correctamente", "data": resultado}), 200

    def delete(uuid):
        resultado = RolServices.delete(uuid)
        if resultado == 404:
            return jsonify({"mensaje": "No se encontró rol"}), 404
        return jsonify({"mensaje": "Rol eliminado correctamente"}), 200
