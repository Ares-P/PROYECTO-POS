from flask import current_app
import uuid
from Models.Mesa import Mesa

class MesaServices:

    def add(data):
        uuid_mes = uuid.uuid4()
        c = current_app.mysql.connection.cursor()
        query = """
            INSERT INTO MESA (MES_UUID, MES_NOMBRE, MES_CAPACIDAD, MES_ESTADO)
            VALUES (%s, %s, %s, %s)
        """
        c.execute(query, (uuid_mes, data["nombre"], data["capacidad"], data["estado"]))
        current_app.mysql.connection.commit()
        id = c.lastrowid
        c.close()
        return {"id": id, "uuid": uuid_mes, "nombre": data["nombre"], "capacidad": data["capacidad"], "estado": data["estado"]}

    def delete(uuid):
        c = current_app.mysql.connection.cursor()
        c.execute("DELETE FROM MESA WHERE MES_UUID = %s", (uuid,))
        current_app.mysql.connection.commit()
        if c.rowcount == 0:
            c.close()
            return 404
        c.close()
        return 200

    def update(uuid, data):
        c = current_app.mysql.connection.cursor()
        query = """
            UPDATE MESA SET
                MES_NOMBRE = %s, MES_CAPACIDAD = %s, MES_ESTADO = %s
            WHERE MES_UUID = %s
        """
        c.execute(query, (data["nombre"], data["capacidad"], data["estado"], uuid))
        current_app.mysql.connection.commit()
        if c.rowcount == 0:
            c.close()
            return 404
        c.close()
        return {"uuid": uuid, **data}

    def consult():
        c = current_app.mysql.connection.cursor()
        c.execute("SELECT * FROM MESA")
        data = c.fetchall()
        c.close()
        return [Mesa(w[0], w[1], w[2], w[3], w[4]).to_dict() for w in data]
