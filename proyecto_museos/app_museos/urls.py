from django.urls import path
from .views import lista_museos

urlpatterns = [
    path('', lista_museos, name='lista_museos'),  # Ruta para la lista de museos
]