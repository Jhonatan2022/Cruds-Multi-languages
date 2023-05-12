# Importamos render y redirect para las vistas
from django.shortcuts import render, redirect

# Importamos el modelo de la base de datos
from .models import Programer   

# Importamos JsonResponse para devolver datos en formato json
from django.http.response import JsonResponse
#-----------------------IMPORT LIBRERIAS AND MODELS---------------------------#




#-----------------------VIEWS-------------------------------------------------#
# Funcion para la vista de inicio
def index(request):

    # Retornamos la vista con los datos
    return render(request, 'index.html')




# Creamos una función para devolver la listas de los programadores
# Usamos el _request para que no nos de error, indicando que no usa el request
def list_programers(_request):

    # Obtenemos los valores de programer
    # List nos devuelve una lista de diccionarios con los valores de programer
    programers = list(Programer.objects.values())

    # Guardamos los datos en un diccionario para enviarlos a la vista
    data = {

        # Guardamos los datos en la llave programer
        'programers': programers
    }

    # Retornamos la vista con los datos en formato json para consumirlos en el front
    return JsonResponse(data)

