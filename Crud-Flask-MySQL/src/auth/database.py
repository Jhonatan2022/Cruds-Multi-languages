# Importamso mysql.connector para poder conectarnos a la base de datos
import mysql.connector

# ---------------------------------IMPORT LIBRARIES---------------------------#


# ---------------------------------CONNECTION---------------------------------#
# Creamos la instancia de la base de datos y le pasamos los parámetros de conexión
database = mysql.connector.connect(
    # host: dirección del servidor
    host="localhost",
    # user: usuario de la base de datos
    user="root",
    # password: contraseña del usuario
    password="",
    # database: nombre de la base de datos
    database="anime",
)
# ---------------------------------CONNECTION------------------------------#
