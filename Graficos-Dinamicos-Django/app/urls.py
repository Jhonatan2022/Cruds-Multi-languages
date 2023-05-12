# Importamos path para definir las rutas de la app
from django.urls import path

# Importamos las vistas de la app
from . import views
#---------------------------------------------------------------




#---------------------------------------------------------------
# Creamos las rutas de nuestra app
urlpatterns = [

    # Definimos la ruta de la vista index
    path('', views.index, name='index'),

    # Definimos la ruta de la vista bar_chart
    path('barchart/', views.barchart, name='barchart'),
]