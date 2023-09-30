from django.urls import path
from . import views

# Creamos las rutas de nuestra app
urlpatterns = [
    # Definimos la ruta de la vista index
    path("", views.index, name="index"),
    # Definimos la ruta de la vista bar_chart
    path("barchart/", views.barchart, name="barchart"),
]
