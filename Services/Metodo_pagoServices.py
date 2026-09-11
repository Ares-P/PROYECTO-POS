from flask import current_app
import uuid
from Models.Metodo_pago import Metodo_pago

class Metodo_pagoServices:

    def add(data):
        uuid_met_pag = uuid.uuid4()
        c = current_app.mysql.connection.cursor()

        query = """
            INSERT INTO METODO_PAGO
            (
                MET_PAG_UUID,
                MET_PAG_NOMBRE,
                MET_PAG_ESTADO,
                MET_PAG_DESCRIPCION
            )
            VALUES (%s, %s, %s, %s)
        """

        values = (
            uuid_met_pag,
            data["nombre"],
            data["estado"],
            data["descripcion"]
        )

        c.execute(query, values)
        current_app.mysql.connection.commit()
        id = c.lastrowid
        c.close()

        data = { "id":id, "uuid": uuid_met_pag, "nombre": data["nombre"], "estado": data["estado"], "descripcion": data["descripcion"]}
        return data



    def delete(uuid):
        c = current_app.mysql.connection.cursor()

        query = "DELETE FROM METODO_PAGO WHERE MET_PAG_UUID = %s"

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
            UPDATE METODO_PAGO
            SET
                MET_PAG_NOMBRE = %s,
                MET_PAG_ESTADO = %s,
                MET_PAG_DESCRIPCION = %s
            WHERE MET_PAG_UUID = %s
        """

        values = (
            data["nombre"],
            data["estado"],
            data["descripcion"],
            uuid
        )

        c.execute(query, values)
        current_app.mysql.connection.commit()
        c.close()

        return {"Mensaje": "Registro actualizado correctamente"}


    def consult():
        c = current_app.mysql.connection.cursor()

        query = "SELECT * FROM METODO_PAGO"

        c.execute(query)

        data = c.fetchall()

        c.close()

        x = [ Metodo_pago (w[0], w[1], w[2], w[3]).to_dict() for w in data]

        return x
