from flask import current_app
import uuid
from Models.Producto import Producto
class ProductoServices:

    def add(data):
        uuid_pro = uuid.uuid4()
        c = current_app.mysql.connection.cursor()

        query = """
            INSERT INTO PRODUCTO
            (
                PRO_UUID,
                PRO_NOMBRE,
                PRO_DESCRIPCION,
                PRO_PRECIO,
                PRO_DISPONIBLE,
                PRO_ESTADO,
                PRO_CAT_ID
            )
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """

        values = (
            uuid_pro,
            data["nombre"],
            data["descripcion"],
            data["precio"],
            data["diponible"],
            data["estado"],
            data["cat_id"]
        )

        c.execute(query, values)
        current_app.mysql.connection.commit()
        id = c.lastrowid
        c.close()

        data = { "id":id, "uuid": uuid_pro, "nombre": data["nombre"], "descripcion": data["descripcion"], "precio": data["precio"], "disponible": data["disponible"], "estado": data["estado"], "cat_id": data["cat_id"]}
        return data
     

    def delete(uuid):
        c = current_app.mysql.connection.cursor()

        query = "DELETE FROM PRODUCTO WHERE PRO_UUID = %s"

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
            UPDATE PRODUCTO
            SET
                PRO_NOMBRE = %s,
                PRO_DESCRIPCION = %s,
                PRO_PRECIO = %s,
                PRO_DISPONIBLE = %s,
                PRO_ESTADO = %s,
                PRO_CAT_ID = %s
            WHERE PRO_UUID = %s
        """

        values = (
            data["nombre"],
            data["descripcion"],
            data["precio"],
            data["disponible"],
            data["estado"],
            data["cat_id"],
            uuid
        )

        c.execute(query, values)
        current_app.mysql.connection.commit()
        c.close()

        return {"Mensaje": "Registro actualizado correctamente"}

    def consult():
        c = current_app.mysql.connection.cursor()

        query = "SELECT * FROM PRODUCTO"

        c.execute(query)

        data = c.fetchall()

        c.close()

        x = [ Producto (w[0], w[1], w[2], w[3]).to_dict() for w in data]

        return x
