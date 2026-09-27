import json
from pathlib import Path
from django.shortcuts import render

BASE_DIR = Path(__file__).resolve().parent

def inicio(request):
    return render(request, 'videojuegos/inicio.html')

def catalogo(request):
    ruta_json = BASE_DIR / 'data' / 'juegos.json'
    with open(ruta_json, encoding='utf-8') as archivo:
        juegos = json.load(archivo)
    return render(request, 'videojuegos/catalogo.html', {'juegos': juegos})
