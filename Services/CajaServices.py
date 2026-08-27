from flask import current_app

class CajaServices:

    def add(data):
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
            data["CAJ_UUID"],
            data["CAJ_ID_CAJA"],
            data["CAJ_FECHA_APERTURA"],
            data["CAJ_ESTADO"],
            data["CAJ_SALDO_INICIAL"],
            data["CAJ_SALDO_FINAL"],
            data["CAJ_FECHA_CIERRE"]
        )

        c.execute(query, values)
        current_app.mysql.connection.commit()
        c.close()

        return {"Mensaje": "Registro agregado correctamente"}


    def delete(id):
        c = current_app.mysql.connection.cursor()

        query = "DELETE FROM CAJA WHERE CAJ_ID = %s"

        c.execute(query, (id,))
        current_app.mysql.connection.commit()
        c.close()

        return {"Mensaje": "Registro eliminado correctamente"}


    def update(id, data):
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
            WHERE CAJ_ID = %s
        """

        values = (
            data["CAJ_ID_CAJA"],
            data["CAJ_FECHA_APERTURA"],
            data["CAJ_ESTADO"],
            data["CAJ_SALDO_INICIAL"],
            data["CAJ_SALDO_FINAL"],
            data["CAJ_FECHA_CIERRE"],
            id
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

        c.close()

        return data
