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
# Methods GET
@app.route('/')
def index():
    products = db['products']
    productsReceived = products.find()
    return render_template('index.html', products=productsReceived)




# Methods POST
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
        return redirect(url_for('index'))
    else:
        return notFound()




# Methods delete
@app.route('/delete/<string:product_name>', methods=['POST'])
def delete(product_name):
    products = db['products']
    products.delete_one({'name': product_name})
    return redirect(url_for('index'))




# Metod PUT
@app.route('/edit/<string:product_name>', methods=['POST'])
def editProduct(product_name):
    products = db['products']
    name = request.form['name']
    price = request.form['price']
    quantity = request.form['quantity']


    if name and price and quantity:
        # Validamos que los campos no estén vacíos
        products.update_one({'name': product_name}, {'$set': {
            'name': name,
            'price': price,
            'quantity': quantity
        }})

        response = jsonify({
            'message': 'Product' + product_name + 'updated successfully',  
        })

        # Redireccionamos a la página principal
        return redirect(url_for('index'))
    else:
        return notFound()




@app.errorhandler(404)
def notFound(error=None):
    mesaage = {
        'message': 'Resource not found' + request.url,
        'status': 404
    }
    response = jsonify(mesaage)
    response.status_code = 404
    return response




if __name__ == '__main__':
    app.run(debug=True, port=8000)
