from flask import current_app
import uuid
from Models.Mesa import Mesa

class MesaServices:

    def add(data):
        c = current_app.mysql.connection.cursor()

        query = """
            INSERT INTO MESA
            (
                MES_UUID,
                MES_NOMBRE,
                MES_CAPACIDAD,
                MES_ESTADO
            )
            VALUES (%s, %s, %s, %s)
        """

        values = (
            data["MES_UUID"],
            data["MES_NOMBRE"],
            data["MES_CAPACIDAD"],
            data["MES_ESTADO"]
        )

        c.execute(query, values)
        current_app.mysql.connection.commit()
        c.close()

        return {"Mensaje": "Registro agregado correctamente"}


    def delete(id):
        c = current_app.mysql.connection.cursor()

        query = "DELETE FROM MESA WHERE MES_ID = %s"

        c.execute(query, (id,))
        current_app.mysql.connection.commit()
        c.close()

        return {"Mensaje": "Registro eliminado correctamente"}


    def update(id, data):
        c = current_app.mysql.connection.cursor()

        query = """
            UPDATE MESA
            SET
                MES_NOMBRE = %s,
                MES_CAPACIDAD = %s,
                MES_ESTADO = %s
            WHERE MES_ID = %s
        """

        values = (
            data["MES_NOMBRE"],
            data["MES_CAPACIDAD"],
            data["MES_ESTADO"],
            id
        )

        c.execute(query, values)
        current_app.mysql.connection.commit()
        c.close()

        return {"Mensaje": "Registro actualizado correctamente"}


    def consult():
        c = current_app.mysql.connection.cursor()

        query = "SELECT * FROM MESA"

        c.execute(query)

        data = c.fetchall()

        c.close()

        x = [ Mesa (w[0], w[1], w[2], w[3]).to_dict() for w in data]

        return x
