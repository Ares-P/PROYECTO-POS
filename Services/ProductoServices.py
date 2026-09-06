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
                PRO_ESTADO
            )
            VALUES (%s, %s, %s, %s, %s, %s)
        """

        values = (
            uuid_pro,
            data["nombre"],
            data["descripcion"],
            data["precio"],
            data["diponible"],
            data["estado"]
        )

        c.execute(query, values)
        current_app.mysql.connection.commit()
        id = c.lastrowid
        c.close()

        data = { "id":id, "uuid": uuid_pro, "PRO_NOMBRE": data["PRO_NOMBRE"], "PRO_DESCRIPCION": data["PRO_DESCRIPCION"], "PRO_PRECIO": data["PRO_PRECIO"], "PRO_DISPONIBLE": data["PRO_DISPONIBLE"], "PRO_ESTADO": data["PRO_ESTADO"]}
        return data
     

    def delete(id):
        c = current_app.mysql.connection.cursor()

        query = "DELETE FROM PRODUCTO WHERE PRO_ID = %s"

        c.execute(query, (id,))
        current_app.mysql.connection.commit()
        c.close()

        return {"Mensaje": "Registro eliminado correctamente"}


    def update(id, data):
        c = current_app.mysql.connection.cursor()

        query = """
            UPDATE PRODUCTO
            SET
                PRO_NOMBRE = %s,
                PRO_DESCRIPCION = %s,
                PRO_PRECIO = %s,
                PRO_DISPONIBLE = %s,
                PRO_ESTADO = %s
            WHERE PRO_ID = %s
        """

        values = (
            data["nombre"],
            data["descripcion"],
            data["precio"],
            data["dispoible"],
            data["estado"],
            id
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
