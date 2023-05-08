# Importamos la libreria Flask para crear la API
from flask import Flask

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
dbs = mongo.db.users
#---------------------------------CONFIGURATIONS---------------------------------#




#---------------------------------ROUTES---------------------------------#
# Definimos la ruta principal de la aplicación
@app.route('/')

# Definimos la función que se ejecutará cuando se entre a la ruta principal
def index():

    # Retornamos un mensaje de bienvenida
    return 'Hello World!'




#---------------------------------RUNNING SERVER---------------------------------#
# Inicializamos la aplicación, pasando como parámetro la instancia de Flask
if __name__ == '__main__':

    # debug=True para que se reinicie el servidor automáticamente cuando se haga un cambio
    app.run(debug=True)