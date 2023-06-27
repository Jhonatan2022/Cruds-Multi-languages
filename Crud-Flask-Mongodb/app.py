# Importamos flask y render_template
from flask import Flask, render_template, request, redirect, url_for, jsonify

# Impotamos la conexión a la base de datos
import database as dbase

# Importamos la clase de productos
from products import Product
#------------------------------------IMPORT FLASK------------------------------------#


# Creamos una instancia de la conexión a la base de datos
db = dbase.dbConnection()


# Damos nombre a la aplicación
app = Flask(__name__)



#------------------------------------ROUTES------------------------------------#
@app.route('/')
def index():
    return render_template('index.html')



@app.route('/products', methods=['POST'])
def addProduct():
    # Creamos la colección de productos si no existe
    products = db['products']
    name = request.form['name']
    price = request.form['price']
    quantity = request.form['quantity']


    # Validamos que los campos no estén vacíos
    if name and price and quantity:
        product = Product(name, price, quantity)
        products.insert_one(product.toCollection())
        response = jsonify({
            'message': 'Product created successfully',
            'name': name,
            'price': price,
            'quantity': quantity
        })




if __name__ == '__main__':
    app.run(debug=True, port=8000)
