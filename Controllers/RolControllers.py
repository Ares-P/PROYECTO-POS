from flask import jsonify, request
from Services.RolServices import RolServices


class RolControllers:

    def consult():
        data = RolServices.consult()
        return jsonify({"mensaje":data}), 200

    def add():
        data = request.get_json(silent=True)
        if not data:
            return jsonify({"Mensaje": "el cuerpo esta vacio o invalido"}), 400

        requeridos = ["nombre", "descripcion"]
        falta = [x for x in requeridos if x not in data]
        if falta:
            return jsonify({"mensaje": f"Faltan parametros{falta}"}), 400

        x = RolServices.add(data)
        return jsonify({"mensaje": "Se registro correctamente", "data": x}), 200

    def update(uuid):
        body_data = request.get_json(silent=True)
        if not body_data:
            return jsonify({"Mensaje": "el cuerpo esta vacio o invalido"}), 400

        result = RolServices.update(uuid, body_data)
        if result == 404:
            return jsonify({"Mensaje": "no se encontro el rol"}), 404
        return jsonify({"mensaje": "Rol actualizado correctamente", "data": result}), 200

    def delete(uuid):
        x = RolServices.delete(uuid)
        if x == 404:
            return jsonify({"Mensaje": "no se encontro el rol"}), x
        else:
            return jsonify({"mensaje": "Rol eliminado correctamente"}), x
