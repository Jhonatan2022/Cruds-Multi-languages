# Importamos JsonResponse para poder retornar un json
from django.http import JsonResponse

# Importamos render para poder renderizar las vistas
from django.shortcuts import render

# Importamos randrange para poder generar numeros aleatorios
from random import randrange
#-------------------------------------------------------------




#-------------------------------------------------------------
# Creamos la vista principal
def index(request):

    # Retornamos la vista index.html
    return render(request, 'index.html')




# Creamos la vista para el grafico de barras
# Colocamos _request como parametro para que no nos de error al no estar usando el parametro en la funcion
def barchart(_request):

    # Creamos una lista vacia
    series = []

    # Creamos un contador que con valor predeterminado 0
    counter = 0

    # mientras el contador sea menor a 7 se ejecutara el ciclo
    while counter < 7:

        # Usamos randrange para generar un numero aleatorio entre 100 y 300 y los agregamos a la lista series
        series.append(randrange(100, 300))


    # Creamos un diccionario
    data = {

        # Creamos una lista con los datos de las etiquetas
        # Usamos xAxis para definir las etiquetas del eje x por medio de apache echarts
        'xAxis':[

            # Creamos un diccionario con los datos de cada etiqueta
            {
                # Category la usamos más para texto
                'type': 'category',
                'data': ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado', 'Domingo']
            }
        ],

        # Usamos yAxis para definir las etiquetas del eje y por medio de apache echarts
        'yAxis':[

            # Creamos un objeto en tipo value para definir los valores del eje y
            {
                # Value lo usamos más para numeros
                'type': 'value'
            }

        ],

        # Creamos una lista con los datos de las series
        # Usamos series para definir las series del grafico por medio de apache echarts
        'series': [
            {
                # Data la usamos para definir los datos de cada serie
                'data': series,
                # Type la usamos para definir el tipo de grafico
                'type': 'line'
            }
        ]

    }

    # Retornamos el diccionario en formato json
    return JsonResponse(data)