from flask import current_app
import uuid
from Models.Metodo_pago import Metodo_pago

class Metodo_pagoServices:

    def add(data):
        uuid_met_pag = uuid.uuid4()
        c = current_app.mysql.connection.cursor()
        query = """
            INSERT INTO METODO_PAGO (MET_PAG_UUID, MET_PAG_NOMBRE, MET_PAG_ESTADO, MET_PAG_DESCRIPCION)
            VALUES (%s, %s, %s, %s)
        """
        c.execute(query, (uuid_met_pag, data["nombre"], data["estado"], data["descripcion"]))
        current_app.mysql.connection.commit()
        id = c.lastrowid
        c.close()
        return {"id": id, "uuid": uuid_met_pag, "nombre": data["nombre"], "estado": data["estado"], "descripcion": data["descripcion"]}

    def delete(uuid):
        c = current_app.mysql.connection.cursor()
        c.execute("DELETE FROM METODO_PAGO WHERE MET_PAG_UUID = %s", (uuid,))
        current_app.mysql.connection.commit()
        if c.rowcount == 0:
            c.close()
            return 404
        c.close()
        return 200

    def update(uuid, data):
        c = current_app.mysql.connection.cursor()
        query = """
            UPDATE METODO_PAGO SET
                MET_PAG_NOMBRE = %s, MET_PAG_ESTADO = %s, MET_PAG_DESCRIPCION = %s
            WHERE MET_PAG_UUID = %s
        """
        c.execute(query, (data["nombre"], data["estado"], data["descripcion"], uuid))
        current_app.mysql.connection.commit()
        if c.rowcount == 0:
            c.close()
            return 404
        c.close()
        return {"uuid": uuid, **data}

    def consult():
        c = current_app.mysql.connection.cursor()
        c.execute("SELECT * FROM METODO_PAGO")
        data = c.fetchall()
        c.close()
        return [Metodo_pago(w[0], w[1], w[2], w[3], w[4]).to_dict() for w in data]
