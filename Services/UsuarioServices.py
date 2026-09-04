from flask import current_app
import uuid
from Models.Usuario import Usuario

class UsuarioServices:

    def add(data):
        uuid_usu = uuid.uuid4()
        c = current_app.mysql.connection.cursor()

        query = """
            INSERT INTO USUARIO
            (
                USU_UUID,
                USU_NOMBRE,
                USU_USUARIO,
                USU_CONTRASENA,
                USU_ESTADO
            )
            VALUES (%s, %s, %s, %s, %s)
        """

        values = (
            uuid_usu,
            data["nombre"],
            data["usuario"],
            data["contrasena"],
            data["estado"]
        )

        c.execute(query, values)
        current_app.mysql.connection.commit()
        id = c.lastrowid
        c.close()

        data = { "id":id, "uuid": uuid_usu, "USU_NOMBRE": data["USU_NOMBRE"], "USU_USUARIO": data["USU_USUARIO"], "USU_CONTRASENA": data["USU_CONTRASENA"], "USU_ESTADO": data["USU_ESTADO"]}
        return data
        


    def delete(id):
        c = current_app.mysql.connection.cursor()

        query = "DELETE FROM USUARIO WHERE USU_ID = %s"

        c.execute(query, (id,))
        current_app.mysql.connection.commit()
        c.close()

        return {"Mensaje": "Registro eliminado correctamente"}


    def update(id, data):
        c = current_app.mysql.connection.cursor()

        query = """
            UPDATE USUARIO
            SET
                USU_NOMBRE = %s,
                USU_USUARIO = %s,
                USU_CONTRASENA = %s,
                USU_ESTADO = %s
            WHERE USU_ID = %s
        """

        values = (
            data["nombre"],
            data["usuario"],
            data["contraseña"],
            data["estado"],
            id
        )

        c.execute(query, values)
        current_app.mysql.connection.commit()
        c.close()

        return {"Mensaje": "Registro actualizado correctamente"}


    def consult():
        c = current_app.mysql.connection.cursor()

        query = "SELECT * FROM USUARIO"

        c.execute(query)

        data = c.fetchall()

        c.close()

        x = [ Usuario (w[0], w[1], w[2], w[3]).to_dict() for w in data]

        return x


