from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Ruta para la vista del administrador de Django
    path("admin/", admin.site.urls),
    # Incluimos las rutas de la aplicacion
    path("app/", include("app.urls")),
]
