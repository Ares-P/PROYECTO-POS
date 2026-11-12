from flask import current_app
import uuid
from Models.Usuario import Usuario

class UsuarioServices:

    def add(data):
        uuid_usu = str(uuid.uuid4())
        c = current_app.mysql.connection.cursor()
        query = """
            INSERT INTO USUARIO
            (USU_UUID, USU_NOMBRE, USU_USUARIO, USU_CONTRASENA, USU_ESTADO, USU_ROL_ID)
            VALUES (%s, %s, %s, %s, %s, %s)
        """
        values = (uuid_usu, data["nombre"], data["usuario"], data["contrasena"], data["estado"], data["rol_id"])
        c.execute(query, values)
        current_app.mysql.connection.commit()
        id = c.lastrowid
        c.close()
        return {"id": id, "uuid": uuid_usu, "nombre": data["nombre"], "usuario": data["usuario"], "contrasena": data["contrasena"], "estado": data["estado"], "rol_id": data["rol_id"]}

    def delete(uuid):
        c = current_app.mysql.connection.cursor()
        c.execute("DELETE FROM USUARIO WHERE USU_UUID = %s", (uuid,))
        current_app.mysql.connection.commit()
        if c.rowcount == 0:
            c.close()
            return 404
        c.close()
        return 200

    def update(uuid, data):
        c = current_app.mysql.connection.cursor()
        query = """
            UPDATE USUARIO SET
                USU_NOMBRE = %s, USU_USUARIO = %s, USU_CONTRASENA = %s,
                USU_ESTADO = %s, USU_ROL_ID = %s
            WHERE USU_UUID = %s
        """
        values = (data["nombre"], data["usuario"], data["contrasena"], data["estado"], data["rol_id"], uuid)
        c.execute(query, values)
        current_app.mysql.connection.commit()
        if c.rowcount == 0:
            c.close()
            return 404
        c.close()
        return {"uuid": uuid, **data}

    def consult():
        c = current_app.mysql.connection.cursor()
        c.execute("SELECT * FROM USUARIO")
        data = c.fetchall()
        c.close()
        return [Usuario(w[0], w[1], w[2], w[3], w[4], w[5], w[6]).to_dict() for w in data]
