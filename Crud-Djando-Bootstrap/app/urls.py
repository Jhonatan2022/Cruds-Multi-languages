# Importamos path para las rutas de las vistas
from django.urls import path

# Importamos las vistas de la aplicacion
from . import views

# -----------------------IMPORT LIBRERIAS AND MODELS---------------------------#


# -----------------------VIEWS-------------------------------------------------#
# Creamos las rutas de las vistas de la aplicacion
urlpatterns = [
    # Ruta para la vista de inicio
    path("", views.index, name="index"),
    # Creamos la vista de list_programers para consumir los datos en el front
    path("list_programers/", views.list_programers, name="list_programers"),
    # # Ruta para la vista de agregar programador
    # path('add/', views.add, name='add'),
    # # Ruta para la vista de editar programador
    # path('edit/<int:id>/', views.edit, name='edit'),
    # # Ruta para la vista de eliminar programador
    # path('delete/<int:id>/', views.delete, name='delete'),
]
