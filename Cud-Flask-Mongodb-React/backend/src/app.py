# Importamos la libreria Flask para crear la API
from flask import (
    
    # Flask: Es la clase que usaremos para crear la API
    Flask,
                   
    # Importamos request para obtener los datos de la petición
    request)

# Importamos pymongo para conectarnos a la base de datos de MongoDB
from flask_pymongo import PyMongo

# Importamos CORS para permitir el acceso a la API desde cualquier origen
from flask_cors import CORS
#---------------------------------IMPORT LIBRARIES---------------------------------#




#---------------------------------CONFIGURATIONS---------------------------------#
# Creamos la instancia de Flask y le pasamos el nombre de la aplicacion
app = Flask(__name__)

# Configuramos la base de datos de MongoDB
app.config['MONGO_URI'] = 'mongodb://localhost/microcrud'

# Creamos la instancia de PyMongo y le pasamos la instancia de Flask
mongo = PyMongo(app)


# Definimos la conección de usuarios y roles
db = mongo.db.users
#---------------------------------CONFIGURATIONS---------------------------------#




#---------------------------------ROUTES---------------------------------#
# Definimos la ruta principal de la aplicación
@app.route('/users', methods=['POST'])
# Definimos la función que se ejecutará cuando se entre a la ruta principal
def createUser():

    # Retornamos un mensaje de bienvenida
    return ''




# Definimos la ruta para crear un nuevo usuario por el metodo GET
@app.route('/users', methods=['GET'])
# Definimos la función que se ejecutará cuando se entre a la ruta principal
def getUsers():

    # Retornamos un mensaje de bienvenida
    return ''




# Definimos la ruta para obtener un solo usuario
@app.route('/users/<id>', methods=['GET'])
# Definimos la función que se ejecutará cuando se entre a la ruta principal
def getUser(id):

    # Retornamos un mensaje de bienvenida
    return ''




# Definimos la ruta para eliminar un usuario
@app.route('/users/<id>', methods=['DELETE'])
# Definimos la función que se ejecutará cuando se entre a la ruta principal
def deleteUser(id):

    # Retornamos un mensaje de bienvenida
    return ''




# Definimos la ruta para actualizar un usuario
# El metodo PUT es para actualizar un recurso
@app.route('/users/<id>', methods=['PUT'])
# Definimos la función que se ejecutará cuando se entre a la ruta principal
def updateUser(id):

    # Retornamos un mensaje de bienvenida
    return ''
#---------------------------------ROUTES---------------------------------#




#---------------------------------RUNNING SERVER---------------------------------#
# Inicializamos la aplicación, pasando como parámetro la instancia de Flask
if __name__ == '__main__':

    # debug=True para que se reinicie el servidor automáticamente cuando se haga un cambio
    app.run(debug=True)