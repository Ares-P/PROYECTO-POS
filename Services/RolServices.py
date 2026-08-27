from flask import current_app

class RolServices:

    def add(data):
        c = current_app.mysql.connection.cursor()

        query = """
            INSERT INTO ROL
            (
                ROL_UUID,
                ROL_NOMBRE,
                ROL_DESCRIPCION
            )
            VALUES (%s, %s, %s)
        """

        values = (
            data["ROL_UUID"],
            data["ROL_NOMBRE"],
            data["ROL_DESCRIPCION"]
        )

        c.execute(query, values)
        current_app.mysql.connection.commit()
        c.close()

        return {"Mensaje": "Registro agregado correctamente"}


    def delete(id):
        c = current_app.mysql.connection.cursor()

        query = "DELETE FROM ROL WHERE ROL_ID = %s"

        c.execute(query, (id,))
        current_app.mysql.connection.commit()
        c.close()

        return {"Mensaje": "Registro eliminado correctamente"}


    def update(id, data):
        c = current_app.mysql.connection.cursor()

        query = """
            UPDATE ROL
            SET
                ROL_NOMBRE = %s,
                ROL_DESCRIPCION = %s
            WHERE ROL_ID = %s
        """

        values = (
            data["ROL_NOMBRE"],
            data["ROL_DESCRIPCION"],
            id
        )

        c.execute(query, values)
        current_app.mysql.connection.commit()
        c.close()

        return {"Mensaje": "Registro actualizado correctamente"}


    def consult():
        c = current_app.mysql.connection.cursor()

        query = "SELECT * FROM ROL"

        c.execute(query)

        data = c.fetchall()

        c.close()

        return data
