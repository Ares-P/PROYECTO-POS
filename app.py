from flask import Flask
from flask_mysqldb import MySQL
from config import Config
from Routes import loadRoutes
from flask_cors import CORS

app = Flask(__name__)

# Permite utilizar rutas con o sin barra final
app.url_map.strict_slashes = False

CORS(app)  # Permite CORS en todas las rutas y orígenes por defecto

app.config.from_object(Config)

mysql = MySQL(app)

app.mysql = mysql

loadRoutes(app)


app.run(debug=True, port=3000, host="0.0.0.0")