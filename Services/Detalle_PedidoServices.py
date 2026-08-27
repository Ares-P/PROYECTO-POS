from flask import current_app
from Models.Detalle_Pedido import Detalle_Pedido

class Detalle_PedidoServices:

    def add(data):
        c = current_app.mysql.connection.cursor()

        query = """
            INSERT INTO DETALLE_PEDIDO
            (
                DET_PED_UUID,
                DET_PED_CANTIDAD,
                DET_PED_PRECIO_UNITARIO,
                DET_PED_SUBTOTAL
            )
            VALUES (%s, %s, %s, %s)
        """

        values = (
            data["DET_PED_UUID"],
            data["DET_PED_CANTIDAD"],
            data["DET_PED_PRECIO_UNITARIO"],
            data["DET_PED_SUBTOTAL"]
        )

        c.execute(query, values)
        current_app.mysql.connection.commit()
        c.close()

        return {"Mensaje": "Registro agregado correctamente"}


    def delete(id):
        c = current_app.mysql.connection.cursor()

        query = "DELETE FROM DETALLE_PEDIDO WHERE DET_PED_ID = %s"

        c.execute(query, (id,))
        current_app.mysql.connection.commit()
        c.close()

        return {"Mensaje": "Registro eliminado correctamente"}


    def update(id, data):
        c = current_app.mysql.connection.cursor()

        query = """
            UPDATE DETALLE_PEDIDO
            SET
                DET_PED_CANTIDAD = %s,
                DET_PED_PRECIO_UNITARIO = %s,
                DET_PED_SUBTOTAL = %s
            WHERE DET_PED_ID = %s
        """

        values = (
            data["DET_PED_CANTIDAD"],
            data["DET_PED_PRECIO_UNITARIO"],
            data["DET_PED_SUBTOTAL"],
            id
        )

        c.execute(query, values)
        current_app.mysql.connection.commit()
        c.close()

        return {"Mensaje": "Registro actualizado correctamente"}


    def consult():
        c = current_app.mysql.connection.cursor()

        query = "SELECT * FROM DETALLE_PEDIDO"

        c.execute(query)

        data = c.fetchall()

        c.close()

        x = [ Detalle_Pedido (w[0], w[1], w[2], w[3]).to_dict() for w in data]

        return x
