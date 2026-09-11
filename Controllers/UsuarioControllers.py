from flask import jsonify, request
from Services.UsuarioServices import UsuarioServices


class UsuarioControllers:

    def consult():
        data = UsuarioServices.consult()
        return jsonify(data), 200

    def create():
        body_data = request.get_json()
        result = UsuarioServices.add(body_data)
        return jsonify({"Mensaje": "Usuario creado correctamente", "data": result}), 201

    def update(uuid):
        body_data = request.get_json(silent=True)
        if not body_data:
            return jsonify({"Mensaje": "el cuerpo esta vacio o invalido"}), 400

        result = UsuarioServices.update(uuid, body_data)
        if result == 404:
            return jsonify({"Mensaje": "no se encontro el usuario"}), 404
        return jsonify({"mensaje": "Usuario actualizado correctamente", "data": result}), 200

    def delete(uuid):
        x = UsuarioServices.delete(uuid)
        if x == 404:
            return jsonify({"Mensaje": "no se encontro el usuario"}), x
        else:
            return jsonify({"mensaje": "Usuario eliminado correctamente"}), x
