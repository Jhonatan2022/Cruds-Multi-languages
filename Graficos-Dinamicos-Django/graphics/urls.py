from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    # Incluimos las urls de la app
    path("", include("app.urls")),
]
