from flask import current_app
import uuid
from Models.Rol import Rol

class RolServices:

    def add(data):
        uuid_rol = uuid.uuid4()
        c = current_app.mysql.connection.cursor()

        query = """
            INSERT INTO ROL
            (
                ROL_UUID,
                ROL_NOMBRE,
                ROL_DESCRIPCION
            )
            VALUES (%s, %s, %s)
        """

        values = (
            uuid_rol,
            data["nombre"],
            data["descripcion"]
        )

        c.execute(query, values)
        current_app.mysql.connection.commit()
        id = c.lastrowid
        c.close()

        data = { "id":id, "uuid": uuid_rol, "Nombre": data["nombre"], "Descripcion": data["descripcion"]}
        return data


    def delete(uuid):
        c = current_app.mysql.connection.cursor()

        query = "DELETE FROM ROL WHERE ROL_UUID = %s"

        c.execute(query, (uuid,))
        current_app.mysql.connection.commit()
        if c.rowcount == 0:
            c.close()
            return 404

        c.close()
        return 200


    def update(uuid, data):
        c = current_app.mysql.connection.cursor()

        query = """
            UPDATE ROL
            SET
                ROL_NOMBRE = %s,
                ROL_DESCRIPCION = %s
            WHERE ROL_UUID = %s
        """

        values = (
            data["nombre"],
            data["descripcion"],
            uuid
        )

        c.execute(query, values)
        current_app.mysql.connection.commit()
        c.close()

        return {"Mensaje": "Registro actualizado correctamente"}


    def consult():
        c = current_app.mysql.connection.cursor()

        query = "SELECT * FROM ROL"

        c.execute(query)

        data = c.fetchall()

        c.close()

        x = [ Rol (w[0], w[1], w[2], w[3]).to_dict() for w in data]

        return x
