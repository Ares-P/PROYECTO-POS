from flask import current_app
import uuid
from Models.Pedido import Pedido

class PedidoServices:

    def add(data):
        uuid_ped = uuid.uuid4()
        c = current_app.mysql.connection.cursor()

        query = """
            INSERT INTO PEDIDO
            (
                PED_UUID,
                PED_DESCUENTO,
                PED_IMPUESTO,
                PED_TOTAL,
                PED_FECHA_HORA,
                PED_NUMERO_ORDEN,
                PED_METODO_ENTREGA,
                PED_SUBTOTAL
            )
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """

        values = (
            uuid_ped,
            data["descuento"],
            data["impuesto"],
            data["total"],
            data["fecha_hora"],
            data["numero_orden"],
            data["metodo_entrega"],
            data["subtotal"]
        )

        c.execute(query, values)
        current_app.mysql.connection.commit()
        id = c.lastrowid
        c.close()

        data = { "id":id, "uuid": uuid_ped, "PED_DESCUENTO": data["PED_DESCUENTO"], "PED_IMPUESTO": data["PED_IMPUESTO"], "PED_TOTAL": data["PED_TOTAL"], "PED_FECHA_HORA": data["PED_FECHA_HORA"], "PED_NUMERO_ORDEN": data["PED_NUMERO_ORDEN"], "PED_METODO_ENTREGA": data["PED_METODO_ENTREGA"], "PED_SUBTOTAL": data["PED_SUBTOTAL"]}
        return data
      


    def delete(id):
        c = current_app.mysql.connection.cursor()

        query = "DELETE FROM PEDIDO WHERE PED_ID = %s"

        c.execute(query, (id,))
        current_app.mysql.connection.commit()
        c.close()

        return {"Mensaje": "Registro eliminado correctamente"}


    def update(id, data):
        c = current_app.mysql.connection.cursor()

        query = """
            UPDATE PEDIDO
            SET
                PED_DESCUENTO = %s,
                PED_IMPUESTO = %s,
                PED_TOTAL = %s,
                PED_FECHA_HORA = %s,
                PED_NUMERO_ORDEN = %s,
                PED_METODO_ENTREGA = %s,
                PED_SUBTOTAL = %s
            WHERE PED_ID = %s
        """

        values = (
            data["descuento"],
            data["impuesto"],
            data["total"],
            data["fecha_hora"],
            data["numero_orden"],
            data["metodo_entrega"],
            data["subtotal"],
            id
        )

        c.execute(query, values)
        current_app.mysql.connection.commit()
        c.close()

        return {"Mensaje": "Registro actualizado correctamente"}


    def consult():
        c = current_app.mysql.connection.cursor()

        query = "SELECT * FROM PEDIDO"

        c.execute(query)

        data = c.fetchall()

        c.close()

        x = [ Pedido (w[0], w[1], w[2], w[3]).to_dict() for w in data]

        return x
