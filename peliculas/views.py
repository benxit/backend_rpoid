import json
from pathlib import Path
from django.shortcuts import render

BASE_DIR = Path(__file__).resolve().parent

def inicio(request):
    return render(request, 'peliculas/inicio.html')

def catalogo(request):
    ruta_json = BASE_DIR / 'data' / 'peliculas.json'
    with open(ruta_json, encoding='utf-8') as archivo:
        peliculas = json.load(archivo)
    return render(request, 'peliculas/catalogo.html', {'peliculas': peliculas})
