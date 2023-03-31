# Importamos las librerias necesarias
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello Word'

if __name__ == "__main__":
    app.run()