import requests
from django.shortcuts import render

def lista_museos(request):
    response = requests.get('https://www.cultura.gob.ar/api/v2.0/museos/')
    datos_museos = response.json().get('results', [])
    return render(request, 'museos/lista_museos.html', {'museos': datos_museos})