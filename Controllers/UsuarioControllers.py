from flask import jsonify, request
from Services.UsuarioServices import UsuarioServices


class UsuarioControllers:

    def consult():
        data = UsuarioServices.consult()
        return jsonify({"mensaje": data}), 200

    def create():
        data = request.get_json(silent=True)
        if not data or not isinstance(data, dict):
            return jsonify({"mensaje": "El cuerpo está vacío o no contiene un JSON válido"}), 400

        requeridos = ['nombre', 'usuario', 'contrasena', 'estado', 'rol_id']
        falta = [campo for campo in requeridos if campo not in data or data[campo] is None or (isinstance(data[campo], str) and not data[campo].strip())]
        if falta:
            return jsonify({"mensaje": f"Faltan parámetros obligatorios: {falta}"}), 400

        resultado = UsuarioServices.add(data)
        return jsonify({"mensaje": "Usuario creado correctamente", "data": resultado}), 201

    def update(uuid):
        body_data = request.get_json(silent=True)
        if not body_data or not isinstance(body_data, dict):
            return jsonify({"mensaje": "El cuerpo está vacío o no contiene un JSON válido"}), 400

        requeridos = ['nombre', 'usuario', 'contrasena', 'estado', 'rol_id']
        falta = [campo for campo in requeridos if campo not in body_data or body_data[campo] is None or (isinstance(body_data[campo], str) and not body_data[campo].strip())]
        if falta:
            return jsonify({"mensaje": f"Faltan parámetros obligatorios: {falta}"}), 400

        resultado = UsuarioServices.update(uuid, body_data)
        if resultado == 404:
            return jsonify({"mensaje": "No se encontró usuario"}), 404
        return jsonify({"mensaje": "Usuario actualizado correctamente", "data": resultado}), 200

    def delete(uuid):
        resultado = UsuarioServices.delete(uuid)
        if resultado == 404:
            return jsonify({"mensaje": "No se encontró usuario"}), 404
        return jsonify({"mensaje": "Usuario eliminado correctamente"}), 200
