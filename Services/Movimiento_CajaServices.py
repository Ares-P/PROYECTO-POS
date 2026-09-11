from flask import current_app
import uuid
from Models.Movimiento_Caja import Movimiento_Caja

class Movimiento_CajaServices:

    def add(data):
        uuid_mov_caj = uuid.uuid4()
        c = current_app.mysql.connection.cursor()

        query = """
            INSERT INTO MOVIMIENTO_CAJA
            (
                MOV_CAJ_UUID,
                MOV_CAJ_TIPO_MOVIMIENTO,
                MOV_CAJ_MONTO,
                MOV_CAJ_DESCRIPCION,
                MOV_CAJ_FECHA_HORA,
                MOV_CAJ_CAJ_ID
            )
            VALUES (%s, %s, %s, %s, %s, %s)
        """

        values = (
            uuid_mov_caj,
            data["tipo_movimiento"],
            data["monto"],
            data["descripcion"],
            data["fecha_hora"],
            data["caj_id"]
        )

        c.execute(query, values)
        current_app.mysql.connection.commit()
        id = c.lastrowid
        c.close()

        data = { "id":id, "uuid": uuid_mov_caj, "tipo_movimiento": data["tipo_movimiento"], "monto": data["monto"], "descripcion": data["descripcion"], "fecha_hora": data["fecha_hora"], "caj_id": data["caj_id"]}
        return data
    


    def delete(uuid):
        c = current_app.mysql.connection.cursor()

        query = "DELETE FROM MOVIMIENTO_CAJA WHERE MOV_CAJ_UUID = %s"

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
            UPDATE MOVIMIENTO_CAJA
            SET
                MOV_CAJ_TIPO_MOVIMIENTO = %s,
                MOV_CAJ_MONTO = %s,
                MOV_CAJ_DESCRIPCION = %s,
                MOV_CAJ_FECHA_HORA = %s,
                MOV_CAJ_CAJ_ID = %s
            WHERE MOV_CAJ_UUID = %s
        """

        values = (
            data["tipo_movimiento"],
            data["monto"],
            data["descripcion"],
            data["fecha_hora"],
            data["caj_id"],
            uuid
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
