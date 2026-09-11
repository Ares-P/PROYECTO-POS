from flask import current_app
import uuid
from Models.Detalle_Pedido import Detalle_Pedido

class Detalle_PedidoServices:

    def add(data):
        uuid_det_ped = uuid.uuid4()
        c = current_app.mysql.connection.cursor()

        query = """
            INSERT INTO DETALLE_PEDIDO
            (
                DET_PED_UUID,
                DET_PED_CANTIDAD,
                DET_PED_PRECIO_UNITARIO,
                DET_PED_SUBTOTAL,
                DET_PED_PED_ID,
                DET_PED_PRO_ID 
            )
            VALUES (%s, %s, %s, %s, %s, %s)
        """

        values = (
            uuid_det_ped,
            data["cantidad"],
            data["precio_unitario"],
            data["subtotal"],
            data["ped_id"],
            data["pro_id"]
        )

        c.execute(query, values)
        current_app.mysql.connection.commit()
        id = c.lastrowid
        c.close()

        data = { "id":id, "uuid": uuid_det_ped, "cantidad": data["cantidad"], "precio_unitario": data["precio_unitario"], "subtotal": data["subtotal"], "ped_id": data["ped_id"], "pro_id":data["pro_id"]}
        return data
       


    def delete(uuid):
        c = current_app.mysql.connection.cursor()

        query = "DELETE FROM DETALLE_PEDIDO WHERE DET_PED_UUID = %s"

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
            UPDATE DETALLE_PEDIDO
            SET
                DET_PED_CANTIDAD = %s,
                DET_PED_PRECIO_UNITARIO = %s,
                DET_PED_SUBTOTAL = %s,
                DET_PED_PED_ID = %s,
                DET_PED_PRO_ID = %s
            WHERE DET_PED_UUID = %s
        """

        values = (
            data["cantidad"],
            data["precio_unitario"],
            data["subtotal"],
            data["ped_id"],
            data["pro_id"],
            uuid
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
