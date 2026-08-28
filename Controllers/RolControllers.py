from flask import jsonify, request
from Services.RolServices import RolServices


class RolControllers:

    def consult():
        data = RolServices.consult()
        return jsonify({"mensaje":data}), 200

    def add():

        #validar el cuerpo de la peticion: valido y no sea null
        # validar que todos los parametros sean enviados 
        # que los parametros tengan informacion y el tipo sea correcto 
        # si existe campo foraneo hay que validar que exista ese registro 

        data = request.get_json(silent=True)
        if not data:
           return jsonify ({"Mensaje": "el cuerpo esta vacio o invalido" }), 400
        
        requeridos = ["nombre", "descripcion"]

        falta = [ x for x in requeridos if x not in data ]

        if len(falta) > 0:
            return jsonify({"mensaje": f"Faltan parametros{falta}"}), 400
        
        x = RolServices.add(data)
        return jsonify({"mensaje":"Se registro correctamente", "data":x}), 200

        

    def update(id):
        body_data = request.get_json()
        result = RolServices.update(id, body_data)
        return jsonify({"mensaje":"data"}), 200

    def delete(id):
        result = RolServices.delete(id)
        return jsonify({"mensaje":"data"}), 200
