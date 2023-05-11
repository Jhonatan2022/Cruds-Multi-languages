# Importamos models para poder crear nuestro modelo
from django.db import models
#---------------------IMPORTS LIBRARIES-----------------------------------------




#---------------------CLASS MODELS----------------------------------------------
# Creamos la tabla de programadores
class Programer(models.Model):


    # Creamos el campo nombre de tipo string
    name = models.CharField(max_length=50)


    # Creamos el campo de ciudad de tipo string
    country = models.CharField(max_length=10)


    # Creamos el campo de cumpleaños de tipo date
    birthday = models.DateField()


    # Creamos el campo de puntaje de tipo entero
    # PositiveSmallIntegerField: Solo permite valores positivos de hasta 32767 (2 bytes)
    score = models.PositiveSmallIntegerField()


    # Usamos class meta para darle un nombre a la tabla
    class Meta:

        # Le damos el nombre a la tabla
        db_table = 'programer'



    # Creamos el metodo __str__ para poder mostrar los datos de la tabla
    def __str__(self):
            
            # Retornamos el nombre
            return self.name