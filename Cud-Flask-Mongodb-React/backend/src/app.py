# Importamos la libreria Flask para crear la API
from flask import (
    
    # Flask: Es la clase que usaremos para crear la API
    Flask,
                   
    # Importamos request para obtener los datos de la petición
    request, 
    
    # Importamos jsonify para convertir los datos en un json y poder retornarlos
    jsonify)

# Importamos pymongo para conectarnos a la base de datos de MongoDB
from flask_pymongo import (

    # Importamos PyMongo para conectarnos a la base de datos de MongoDB
    PyMongo, 

    # Importamos ObjectId para poder buscar por id
    ObjectId
)

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

# Pasamos el app a CORS para permitir el acceso a la API desde cualquier origen como react
CORS(app)


# Definimos la conección de usuarios y roles
db = mongo.db.users
#---------------------------------CONFIGURATIONS---------------------------------#




#---------------------------------ROUTES---------------------------------#
# Definimos la ruta principal de la aplicación
@app.route('/users', methods=['POST'])
# Definimos la función que se ejecutará cuando se entre a la ruta principal
def createUser():

    # Obtenemos los datos de la petición y los insertamos en la base de datos
    id = db.insert({
        'username': request.json['username'],
        'name': request.json['name'],
        'age': request.json['age'],
        'email': request.json['email'],
        'password': request.json['password']
    })

    # Retornamos el id del usuario creado usando jsonify para convertirlo en un json
    return jsonify(str(ObjectId(id)))




# Definimos la ruta para crear un nuevo usuario por el metodo GET
@app.route('/users', methods=['GET'])
# Definimos la función que se ejecutará cuando se entre a la ruta principal
def getUsers():

    # Creamos una lista vacia para guardar los usuarios
    users = []

    # Recorremos todos los usuarios de la base de datos
    for doc in db.find():

        # Agregamos los usuarios a la lista
        users.append({
            '_id': str(ObjectId(doc['_id'])),
            'username': doc['username'],
            'name': doc['name'],
            'age': doc['age'],
            'email': doc['email'],
            'password': doc['password']
        })

    # Retornamos la lista de usuarios usando jsonify para convertirlo en un json
    return jsonify(users)




# Definimos la ruta para obtener un solo usuario
@app.route('/users/<id>', methods=['GET'])
# Definimos la función que se ejecutará cuando se entre a la ruta principal
def getUser(id):

    # Buscamos el usuario por id
    # El metodo find_one es para buscar un solo documento en la base de datos
    user = db.find_one({'_id': ObjectId(id)})

    # Retornamos el usuario usando jsonify para convertirlo en un json
    return jsonify({
        '_id': str(ObjectId(user['_id'])),
        'username': user['username'],
        'name': user['name'],
        'age': user['age'],
        'email': user['email'],
        'password': user['password']
    })




# Definimos la ruta para eliminar un usuario
# El metodo DELETE es para eliminar un recurso de la base de datos
@app.route('/users/<id>', methods=['DELETE'])
# Definimos la función que se ejecutará cuando se entre a la ruta principal
def deleteUser(id):

    # Eliminamos el usuario por id
    # El metodo delete_one es para eliminar un solo documento en la base de datos
    db.delete_one({'_id': ObjectId(id)})

    # Retornamos un mensaje de bienvenida
    return ''




# Definimos la ruta para actualizar un usuario
# El metodo PUT es para actualizar un recurso
@app.route('/users/<id>', methods=['PUT'])
# Definimos la función que se ejecutará cuando se entre a la ruta principal
def updateUser(id):

    # Actualizamos el usuario por id
    # El metodo update_one es para actualizar un solo documento en la base de datos
    db.update_one({ '_id': ObjectId(id)}, {
    '$set': {
        'username': request.json['username'],
        'name': request.json['name'],
        'age': request.json['age'],
        'email': request.json['email'],
        'password': request.json['password']
    }})

    # Retornamos un mensaje de bienvenida
    return jsonify({
        'msg': 'User updated'
    })
#---------------------------------ROUTES---------------------------------#




#---------------------------------RUNNING SERVER---------------------------------#
# Inicializamos la aplicación, pasando como parámetro la instancia de Flask
if __name__ == '__main__':

    # debug=True para que se reinicie el servidor automáticamente cuando se haga un cambio
    app.run(debug=True)