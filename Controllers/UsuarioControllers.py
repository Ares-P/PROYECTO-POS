from flask import jsonify, request 
from Services.UsuarioServices import UsuarioServices

class UsuarioControllers:

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


    def update(id):
        body_data = request.get_json()
        result = UsuarioServices.update(id, body_data)
        return jsonify({"Mensaje": "Usuario actualizado correctamente", "data": result}), 200

    def delete(id):
        result = UsuarioServices.delete(id)
        return jsonify({"Mensaje": "Usuario eliminado correctamente"}), 200
