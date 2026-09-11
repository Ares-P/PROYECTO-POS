from flask import current_app
import uuid
from Models.Caja import Caja
class CajaServices:

    def add(data):
        uuid_caj = uuid.uuid4()
        c = current_app.mysql.connection.cursor()

        query = """
            INSERT INTO CAJA
            (
                CAJ_UUID,
                CAJ_ID_CAJA,
                CAJ_FECHA_APERTURA,
                CAJ_ESTADO,
                CAJ_SALDO_INICIAL,
                CAJ_SALDO_FINAL,
                CAJ_FECHA_CIERRE
            )
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """

        values = (
            uuid_caj,
            data["id_caja"],
            data["fecha_apertura"],
            data["estado"],
            data["saldo_inicial"],
            data["saldo_final"],
            data["fecha_cierre"]
        )

        c.execute(query, values)
        current_app.mysql.connection.commit()
        id = c.lastrowid
        c.close()   

        data = { "id":id, "uuid": uuid_caj, "id_caja": data["id_caja"], "fecha_apertura": data["fecha_apertura"], "estado": data["estado"], "saldo_inicial": data["saldo_inicial"], "saldo_final": data["saldo_final"], "fecha_cierre": data["fecha_cierre"]}
        return data
        


    def delete(uuid):
        c = current_app.mysql.connection.cursor()

        query = "DELETE FROM CAJA WHERE CAJ_UUID = %s"

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
            UPDATE CAJA
            SET
                CAJ_ID_CAJA = %s,
                CAJ_FECHA_APERTURA = %s,
                CAJ_ESTADO = %s,
                CAJ_SALDO_INICIAL = %s,
                CAJ_SALDO_FINAL = %s,
                CAJ_FECHA_CIERRE = %s
            WHERE CAJ_UUID = %s
        """

        values = (
            data["id_caja"],
            data["fecha_apertura"],
            data["estado"],
            data["saldo_inicial"],
            data["saldo_final"],
            data["fecha_cierre"],
            uuid
        )

        c.execute(query, values)
        current_app.mysql.connection.commit()
        c.close()

        return {"Mensaje": "Registro actualizado correctamente"}


    def consult():
        c = current_app.mysql.connection.cursor()

        query = "SELECT * FROM CAJA"

        c.execute(query)

        data = c.fetchall()

        x = [ Caja (w[0], w[1], w[2], w[3], w[4], w[5], w[6],w[7] ).to_dict() for w in data]

        return x