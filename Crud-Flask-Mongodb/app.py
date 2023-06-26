# Importamos flask y render_template
from flask import Flask, render_template, request, redirect, url_for

# Damos nombre a la aplicación
app = Flask(__name__)



@app.route('/')
def index():
    return render_template('index.html')



if __name__ == '__main__':
    app.run(debug=True, port=8000)
