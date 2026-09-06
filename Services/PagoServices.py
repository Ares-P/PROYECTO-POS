from flask import current_app
import uuid
from Models.Pago import Pago

class PagoServices:

    def add(data):
        uuid_pag = uuid.uuid4()
        c = current_app.mysql.connection.cursor()

        query = """
            INSERT INTO PAGO
            (
                PAG_UUID,
                PAG_ID_PAGO,
                PAG_REFERENCIA,
                PAG_ESTADO,
                PAG_FECHA_PAGO,
                PAG_VALOR_PAGADO
            )
            VALUES (%s, %s, %s, %s, %s, %s)
        """

        values = (
            uuid_pag,
            data["id_pago"],
            data["referencia"],
            data["estado"],
            data["fecha_pago"],
            data["valor_pagado"]
        )

        c.execute(query, values)
        current_app.mysql.connection.commit()
        id = c.lastrowid
        c.close()

        data = { "id":id, "uuid": uuid_pag, "PAG_ID_PAGO": data["PAG_ID_PAGO"], "PAG_REFERENCIA": data["PAG_REFERENCIA"], "PAG_ESTADO": data["PAG_ESTADO"], "PAG_FECHA_PAGO": data["PAG_FECHA_PAGO"], "PAG_VALOR_PAGADO": data["PAG_VALOR_PAGADO"]}
        return data
       


    def delete(id):
        c = current_app.mysql.connection.cursor()

        query = "DELETE FROM PAGO WHERE PAG_ID = %s"

        c.execute(query, (id,))
        current_app.mysql.connection.commit()
        c.close()

        return {"Mensaje": "Registro eliminado correctamente"}


    def update(id, data):
        c = current_app.mysql.connection.cursor()

        query = """
            UPDATE PAGO
            SET
                PAG_ID_PAGO = %s,
                PAG_REFERENCIA = %s,
                PAG_ESTADO = %s,
                PAG_FECHA_PAGO = %s,
                PAG_VALOR_PAGADO = %s
            WHERE PAG_ID = %s
        """

        values = (
            data["id_pago"],
            data["referencia"],
            data["estado"],
            data["fecha_pago"],
            data["valor_pagado"],
            id
        )

        c.execute(query, values)
        current_app.mysql.connection.commit()
        c.close()

        return {"Mensaje": "Registro actualizado correctamente"}


    def consult():
        c = current_app.mysql.connection.cursor()

        query = "SELECT * FROM PAGO"

        c.execute(query)

        data = c.fetchall()

        c.close()

        x = [ Pago (w[0], w[1], w[2], w[3]).to_dict() for w in data]

        return x
