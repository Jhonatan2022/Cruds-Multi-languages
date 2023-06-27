from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import certifi

uri = "mongodb+srv://florezj328:pymongo@pymongo.yzvpj1k.mongodb.net/?retryWrites=true&w=majority"
ca = certifi.where()


def dbConnection():
    try:
        # Create a new client and connect to the server
        client = MongoClient(uri, tlsCAFile=ca)

        # Creamos una base de datos en caso que no exista
        db = client["db-products"]
    except ConnectionError:
        print("Error connecting to MongoDB")
    return db
