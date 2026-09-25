from flask import current_app
import uuid
from Models.Rol import Rol

class RolServices:

    def add(data):
        uuid_rol = uuid.uuid4()
        c = current_app.mysql.connection.cursor()
        query = """
            INSERT INTO ROL (ROL_UUID, ROL_NOMBRE, ROL_DESCRIPCION)
            VALUES (%s, %s, %s)
        """
        c.execute(query, (uuid_rol, data["nombre"], data["descripcion"]))
        current_app.mysql.connection.commit()
        id = c.lastrowid
        c.close()
        return {"id": id, "uuid": uuid_rol, "nombre": data["nombre"], "descripcion": data["descripcion"]}

    def delete(uuid):
        c = current_app.mysql.connection.cursor()
        c.execute("DELETE FROM ROL WHERE ROL_UUID = %s", (uuid,))
        current_app.mysql.connection.commit()
        if c.rowcount == 0:
            c.close()
            return 404
        c.close()
        return 200

    def update(uuid, data):
        c = current_app.mysql.connection.cursor()
        query = """
            UPDATE ROL SET
                ROL_NOMBRE = %s, ROL_DESCRIPCION = %s
            WHERE ROL_UUID = %s
        """
        c.execute(query, (data["nombre"], data["descripcion"], uuid))
        current_app.mysql.connection.commit()
        if c.rowcount == 0:
            c.close()
            return 404
        c.close()
        return {"uuid": uuid, **data}

    def consult():
        c = current_app.mysql.connection.cursor()
        c.execute("SELECT * FROM ROL")
        data = c.fetchall()
        c.close()
        return [Rol(w[0], w[1], w[2], w[3]).to_dict() for w in data]
