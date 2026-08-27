from flask import current_app
import uuid
from Models.Usuario import Usuario

class UsuarioServices:

    def add(data):
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
            uuid.uuid4(),
            data["USU_NOMBRE"],
            data["USU_USUARIO"],
            data["USU_CONTRASENA"],
            data["USU_ESTADO"]
        )

        c.execute(query, values)
        current_app.mysql.connection.commit()
        c.close()

        return {"Mensaje": "Registro agregado correctamente"}


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
            data["USU_NOMBRE"],
            data["USU_USUARIO"],
            data["USU_CONTRASENA"],
            data["USU_ESTADO"],
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


