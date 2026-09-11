from flask import current_app
import uuid
from Models.Estado_Pedido import Estado_Pedido

class Estado_PedidoServices:

    def add(data):
        uuid_est_ped = uuid.uuid4()
        c = current_app.mysql.connection.cursor()

        query = """
            INSERT INTO ESTADO_PEDIDO
            (
                EST_PED_UUID,
                EST_PED_NOMBRE,
                EST_PED_DESCRIPCION
            )
            VALUES (%s, %s, %s)
        """

        values = (
            uuid_est_ped,
            data["nombre"],
            data["descripcion"]
        )

        c.execute(query, values)
        current_app.mysql.connection.commit()
        id = c.lastrowid
        c.close()

        data = { "id":id, "uuid": uuid_est_ped, "nombre": data["nombre"], "descripcion": data["descripcion"]}
        return data
       


    def delete(uuid):
        c = current_app.mysql.connection.cursor()

        query = "DELETE FROM ESTADO_PEDIDO WHERE EST_PED_UUID = %s"

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
            UPDATE ESTADO_PEDIDO
            SET
                EST_PED_NOMBRE = %s,
                EST_PED_DESCRIPCION = %s
            WHERE EST_PED_UUID = %s
        """

        values = (
            data["nombre"],
            data["descripcion"],
            uuid
        )

        c.execute(query, values)
        current_app.mysql.connection.commit()
        c.close()

        return {"Mensaje": "Registro actualizado correctamente"}


    def consult():
        c = current_app.mysql.connection.cursor()

        query = "SELECT * FROM ESTADO_PEDIDO"

        c.execute(query)

        data = c.fetchall()

        c.close()

        x = [ Estado_Pedido (w[0], w[1], w[2], w[3]).to_dict() for w in data]

        return x
