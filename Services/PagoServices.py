from flask import current_app

class PagoServices:

    def add(data):
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
            data["PAG_UUID"],
            data["PAG_ID_PAGO"],
            data["PAG_REFERENCIA"],
            data["PAG_ESTADO"],
            data["PAG_FECHA_PAGO"],
            data["PAG_VALOR_PAGADO"]
        )

        c.execute(query, values)
        current_app.mysql.connection.commit()
        c.close()

        return {"Mensaje": "Registro agregado correctamente"}


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
            data["PAG_ID_PAGO"],
            data["PAG_REFERENCIA"],
            data["PAG_ESTADO"],
            data["PAG_FECHA_PAGO"],
            data["PAG_VALOR_PAGADO"],
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

        return data
