from flask import current_app
import uuid
from Models.Categoria import Categoria

class CategoriaServices:

    def add(data):
        uuid_cat = uuid.uuid4()
        c = current_app.mysql.connection.cursor()

        query = """
            INSERT INTO CATEGORIA
            (
                CAT_UUID,
                CAT_NOMBRE,
                CAT_DESCRIPCION,
                CAT_ESTADO
            )
            VALUES (%s, %s, %s, %s)
        """

        values = (
            uuid_cat,
            data["nombre"],
            data["descripcion"],
            data["estado"]
        )

        c.execute(query, values)
        current_app.mysql.connection.commit()
        id = c.lastrowid
        c.close()

        data = { "id":id, "uuid": uuid_cat, "nombre": data["nombre"], "descripcion": data["descripcion"], "estado": data["estado"]}
        return data
      


    def delete(uuid):
        c = current_app.mysql.connection.cursor()

        query = "DELETE FROM CATEGORIA WHERE CAT_UUID = %s"

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
            UPDATE CATEGORIA
            SET
                CAT_NOMBRE = %s,
                CAT_DESCRIPCION = %s,
                CAT_ESTADO = %s
            WHERE CAT_UUID = %s
        """

        values = (
            data["nombre"],
            data["descripcion"],
            data["estado"],
            uuid
        )

        c.execute(query, values)
        current_app.mysql.connection.commit()
        c.close()

        return {"Mensaje": "Registro actualizado correctamente"}


    def consult():
        c = current_app.mysql.connection.cursor()

        query = "SELECT * FROM CATEGORIA"

        c.execute(query)

        data = c.fetchall()

        c.close()

        x = [ Categoria (w[0], w[1], w[2], w[3]).to_dict() for w in data]

        return x
