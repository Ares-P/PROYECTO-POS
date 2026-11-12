from flask import current_app
import uuid
from Models.Estado_Pedido import Estado_Pedido

class Estado_PedidoServices:

    def add(data):
        uuid_est_ped = str(uuid.uuid4())
        c = current_app.mysql.connection.cursor()
        query = """
            INSERT INTO ESTADO_PEDIDO (EST_PED_UUID, EST_PED_NOMBRE, EST_PED_DESCRIPCION)
            VALUES (%s, %s, %s)
        """
        c.execute(query, (uuid_est_ped, data["nombre"], data["descripcion"]))
        current_app.mysql.connection.commit()
        id = c.lastrowid
        c.close()
        return {"id": id, "uuid": uuid_est_ped, "nombre": data["nombre"], "descripcion": data["descripcion"]}

    def delete(uuid):
        c = current_app.mysql.connection.cursor()
        c.execute("DELETE FROM ESTADO_PEDIDO WHERE EST_PED_UUID = %s", (uuid,))
        current_app.mysql.connection.commit()
        if c.rowcount == 0:
            c.close()
            return 404
        c.close()
        return 200

    def update(uuid, data):
        c = current_app.mysql.connection.cursor()
        query = """
            UPDATE ESTADO_PEDIDO SET
                EST_PED_NOMBRE = %s, EST_PED_DESCRIPCION = %s
            WHERE EST_PED_UUID = %s
        """
        c.execute(query, (data["nombre"], data["descripcion"], uuid))
        current_app.mysql.connection.commit()
        if c.rowcount == 0:
            c.close()
            return 404
        c.close()
        return {"uuid": uuid, **data}

    def consult():
        c = current_app.mysql.connection.cursor()
        c.execute("SELECT * FROM ESTADO_PEDIDO")
        data = c.fetchall()
        c.close()
        return [Estado_Pedido(w[0], w[1], w[2], w[3]).to_dict() for w in data]
