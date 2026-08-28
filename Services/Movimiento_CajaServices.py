from flask import current_app
import uuid
from Models.Movimiento_Caja import Movimiento_Caja

class Movimiento_CajaServices:

    def add(data):
        c = current_app.mysql.connection.cursor()

        query = """
            INSERT INTO MOVIMIENTO_CAJA
            (
                MOV_CAJ_UUID,
                MOV_CAJ_TIPO_MOVIMIENTO,
                MOV_CAJ_MONTO,
                MOV_CAJ_DESCRIPCION,
                MOV_CAJ_FECHA_HORA
            )
            VALUES (%s, %s, %s, %s, %s)
        """

        values = (
            data["MOV_CAJ_UUID"],
            data["MOV_CAJ_TIPO_MOVIMIENTO"],
            data["MOV_CAJ_MONTO"],
            data["MOV_CAJ_DESCRIPCION"],
            data["MOV_CAJ_FECHA_HORA"]
        )

        c.execute(query, values)
        current_app.mysql.connection.commit()
        c.close()

        return {"Mensaje": "Registro agregado correctamente"}


    def delete(id):
        c = current_app.mysql.connection.cursor()

        query = "DELETE FROM MOVIMIENTO_CAJA WHERE MOV_CAJ_ID = %s"

        c.execute(query, (id,))
        current_app.mysql.connection.commit()
        c.close()

        return {"Mensaje": "Registro eliminado correctamente"}


    def update(id, data):
        c = current_app.mysql.connection.cursor()

        query = """
            UPDATE MOVIMIENTO_CAJA
            SET
                MOV_CAJ_TIPO_MOVIMIENTO = %s,
                MOV_CAJ_MONTO = %s,
                MOV_CAJ_DESCRIPCION = %s,
                MOV_CAJ_FECHA_HORA = %s
            WHERE MOV_CAJ_ID = %s
        """

        values = (
            data["MOV_CAJ_TIPO_MOVIMIENTO"],
            data["MOV_CAJ_MONTO"],
            data["MOV_CAJ_DESCRIPCION"],
            data["MOV_CAJ_FECHA_HORA"],
            id
        )

        c.execute(query, values)
        current_app.mysql.connection.commit()
        c.close()

        return {"Mensaje": "Registro actualizado correctamente"}


    def consult():
        c = current_app.mysql.connection.cursor()

        query = "SELECT * FROM MOVIMIENTO_CAJA"

        c.execute(query)

        data = c.fetchall()

        c.close()

        x = [ Movimiento_Caja (w[0], w[1], w[2], w[3]).to_dict() for w in data]

        return x
