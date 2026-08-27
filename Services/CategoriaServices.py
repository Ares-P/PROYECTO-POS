from flask import current_app

class CategoriaServices:

    def add(data):
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
            data["CAT_UUID"],
            data["CAT_NOMBRE"],
            data["CAT_DESCRIPCION"],
            data["CAT_ESTADO"]
        )

        c.execute(query, values)
        current_app.mysql.connection.commit()
        c.close()

        return {"Mensaje": "Registro agregado correctamente"}


    def delete(id):
        c = current_app.mysql.connection.cursor()

        query = "DELETE FROM CATEGORIA WHERE CAT_ID = %s"

        c.execute(query, (id,))
        current_app.mysql.connection.commit()
        c.close()

        return {"Mensaje": "Registro eliminado correctamente"}


    def update(id, data):
        c = current_app.mysql.connection.cursor()

        query = """
            UPDATE CATEGORIA
            SET
                CAT_NOMBRE = %s,
                CAT_DESCRIPCION = %s,
                CAT_ESTADO = %s
            WHERE CAT_ID = %s
        """

        values = (
            data["CAT_NOMBRE"],
            data["CAT_DESCRIPCION"],
            data["CAT_ESTADO"],
            id
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

        return data
