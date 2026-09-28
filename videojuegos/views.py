from django.shortcuts import render

from .models import Videojuego


def inicio(request):
    return render(request, 'videojuegos/inicio.html')


def catalogo(request):
    query = request.GET.get('q', '').strip()
    juegos = Videojuego.objects.select_related('genero', 'plataforma').all()
    if query:
        juegos = juegos.filter(nombre__icontains=query)
    return render(request, 'videojuegos/catalogo.html', {'juegos': juegos, 'query': query})
