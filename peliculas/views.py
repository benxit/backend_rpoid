from django.shortcuts import render

from .models import Pelicula


def inicio(request):
    return render(request, 'peliculas/inicio.html')


def catalogo(request):
    query = request.GET.get('q', '').strip()
    peliculas = Pelicula.objects.select_related('genero', 'director').all()
    if query:
        peliculas = peliculas.filter(titulo__icontains=query)
    return render(request, 'peliculas/catalogo.html', {'peliculas': peliculas, 'query': query})
