# Importamos admin para poder registrar nuestro modelo
from django.contrib import admin

# Importamos nuestro modelo para poder registrarlos
from .models import Programer
#---------------------IMPORTS LIBRARIES-----------------------------------------




#---------------------CLASS MODELS----------------------------------------------
# Registramos el modelo de programer para que se pueda ver en el admin
admin.site.register(Programer)