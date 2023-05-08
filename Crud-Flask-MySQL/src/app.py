# Importamos la libreria Flask para crear la API
from flask import (

    # Flask: nos permite crear la aplicación
    Flask,

     # render_template: nos permite renderizar los archivos html
    render_template, 
    
    # request: nos permite obtener los datos del formulario
    request, 
    
    # redirect: nos permite redireccionar a otra ruta
    redirect, 
    
    # url_for: nos permite obtener la ruta de una función
    url_for)

# Importamos os para poder acceder a las variables de entorno
import os

# Importamos el archivo database.py para poder conectarnos a la base de datos y le asignamos el alias db
from auth import database as db
#---------------------------------IMPORT LIBRARIES---------------------------------#




#---------------------------------CONFIGURATIONS---------------------------------#
# Creamos la instancia para poder acceder los archivos de la carpeta templates
# dirname: nombre del directorio actual (src)
# abspath: ruta absoluta del directorio actual (Crud-Flask-MySQL\src)
# dirname: nombre del directorio padre (Crud-Flask-MySQL)
template_dir = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))


# Unimos la ruta del directorio padre con la carpeta templates (Crud-Flask-MySQL\templates)
# join: une muchas rutas en una sola 
template_dir = os.path.join(template_dir, 'src', 'templates')


# Creamos la instancia de Flask y le pasamos el nombre de la aplicacion
# template_folder: ruta de la carpeta templates (Crud-Flask-MySQL\templates)
app = Flask(__name__, template_folder=template_dir)
#---------------------------------CONFIGURATIONS---------------------------------#




#---------------------------------ROUTES---------------------------------#
# Definimos la ruta principal de la aplicación (Crud-Flask-MySQL\src\templates\index.html)
@app.route('/')

# Definimos la función home para retornar el archivo index.html
def home():


    # Creamos un objeto de la clase database
    conection = db.database.cursor()

    # Hacemos una consulta a la base de datos donde nos devolverá todos los registros de la tabla users
    # execute: ejecuta una consulta a la base de datos
    conection.execute('SELECT * FROM users')

    # fetchall: devuelve todos los registros de la consulta
    # fetchone: devuelve un registro de la consulta
    # fetchmany: devuelve una cantidad de registros de la consulta
    # Usamos fetchall para obtener todos los registros de la consulta y los guardamos en la variable myresult
    myresult = conection.fetchall()

    # Convertimos los datos en un diccionario
    # Creamos un diccionario vacio
    objects = []

    # Recorremos las columnas para obtener los datos de cada registro
    columNmaes = [column[0] for column in conection.description]

    # Recorremos los registros y los guardamos en el diccionario
    for row in myresult:

        # Usamos append para agregar los datos al diccionario
        # Usamos dict para convertir los datos en un diccionario
        # Usamos zip para unir las columnas con los registros
        objects.append(dict(zip(columNmaes, row)))

    # Cerramos la conexión con la base de datos
    conection.close()
        

    # Retornamos el archivo index.html
    # Le pasamos como parámetro los datos de la base de datos
    return render_template('home.html', data=objects)




# Definimos la ruta para guardar usuarios y le pasamos el metodo POST
@app.route('/save', methods=['POST'])

# Definimos la función save para guardar los datos del formulario
def saveData():

    # Obtenemos los datos del formulario y los guardamos en variables
    user_name = request.form['user_name']
    name = request.form['name']
    email = request.form['email']
    pasword = request.form['pasword']

    # Creamos una condicional para validar que tenemos todos los campos
    if user_name and name and email and pasword:

        # Creamos un objeto de la clase database y usamso cursor para poder ejecutar consultas
        guardo = db.database.cursor()

        # Creamos una consulta para insertar los datos en la base de datos
        # VALUES: valores que se van a insertar en la base de datos
        sql = "INSERT INTO users (user_name, name, email, pasword) VALUES (%s, %s, %s, %s)"

        # Pasamos los datos por medio de una dupla
        data = (user_name, name, email, pasword)

        # Ejecutamos la consulta y pasamos los datos
        # execute: ejecuta una consulta a la base de datos
        guardo.execute(sql, data)

        # Guardamos los cambios en la base de datos
        # commit: guarda los cambios en la base de datos
        db.database.commit()

    # Retornamos la ruta principal de la aplicación
    return redirect(url_for('home'))




# Definimos la ruta para eliminar usuarios y le pasamos el metodo GET
@app.route('/delete/<string:id>')

# Definimos la función delete para eliminar los datos de la base de datos
def deleteData(id):

    # Creamos un objeto de la clase database y usamso cursor para poder ejecutar consultas
    eliminar = db.database.cursor()

    # Creamos una consulta para eliminar los datos de la base de datos
    # WHERE: condición para eliminar los datos
    sql = "DELETE FROM users WHERE id_user = %s"

    # Pasamos los datos por medio de una dupla
    data = (id,)

    # Ejecutamos la consulta y pasamos los datos
    # execute: ejecuta una consulta a la base de datos
    eliminar.execute(sql, data)

    # Guardamos los cambios en la base de datos
    # commit: guarda los cambios en la base de datos
    db.database.commit()

    # Retornamos la ruta principal de la aplicación
    return redirect(url_for('home'))




# Definimos la ruta para editar usuarios y le pasamos el metodo GET
@app.route('/edit/<string:id>', methods=['POST'])

# Definimos la función edit para editar los datos de la base de datos
def editData(id):

    # Obtener los datos del formulario y los guardamos en variables
    user_name = request.form['user_name']
    name = request.form['name']
    email = request.form['email']
    pasword = request.form['pasword']

    # Creamos una condicional para validar que tenemos todos los campos
    if user_name and name and email and pasword:

        # Creamos un objeto de la clase database y usamso cursor para poder ejecutar consultas
        editar = db.database.cursor()

        # Creamos una consulta para editar los datos de la base de datos
        # SET: valores que se van a editar en la base de datos
        # WHERE: condición para editar los datos
        sql = "UPDATE users SET user_name = %s, name = %s, email = %s, pasword = %s WHERE id_user = %s"

        # Pasamos los datos por medio de una dupla
        data = (user_name, name, email, pasword, id)

        # Ejecutamos la consulta y pasamos los datos
        # execute: ejecuta una consulta a la base de datos
        editar.execute(sql, data)

        # Guardamos los cambios en la base de datos
        # commit: guarda los cambios en la base de datos
        db.database.commit()

    # Retornamos la ruta principal de la aplicación
    return redirect(url_for('home'))
#---------------------------------ROUTES---------------------------------#




#---------------------------------RUNNING SERVER---------------------------------#
# Inicializamos la aplicación, pasando como parámetro la instancia de Flask
if __name__ == '__main__':

    # debug=True para que se reinicie el servidor automáticamente cuando se haga un cambio
    # port: nos permite definir el puerto por el cual se ejecutará la aplicación
    app.run(debug=True, port=4000)
#---------------------------------RUNNING SERVER---------------------------------#