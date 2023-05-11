# Importamos render y redirect para las vistas
from django.shortcuts import render, redirect

# Importamos el modelo de la base de datos
from .models import Programer   
#-----------------------IMPORT LIBRERIAS AND MODELS---------------------------#




#-----------------------VIEWS-------------------------------------------------#
# Funcion para la vista de inicio
def index(request):

    # Consultamos todos los registros de la base de datos
    programers = Programer.objects.all()

    # Creamos un diccionario con los datos de la base de datos
    data = {
        'programers': programers
    }

    # Retornamos la vista con los datos
    return render(request, 'app/index.html', data)


