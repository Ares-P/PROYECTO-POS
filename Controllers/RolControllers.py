from flask import jsonify, request
from Services.RolServices import RolServices


class RolControllers:

    def consult():
        data = RolServices.consult()
        return jsonify({"mensaje":data}), 200

    def create():
        body_data = request.get_json()
        result = RolServices.add(body_data)
        return jsonify({"mensaje":"data"}), 200

    def update(id):
        body_data = request.get_json()
        result = RolServices.update(id, body_data)
        return jsonify({"mensaje":"data"}), 200

    def delete(id):
        result = RolServices.delete(id)
        return jsonify({"mensaje":"data"}), 200
