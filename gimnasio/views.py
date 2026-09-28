from django.shortcuts import render

from .models import Equipo


def inicio(request):
    return render(request, 'gimnasio/inicio.html')


def catalogo(request):
    query = request.GET.get('q', '').strip()
    equipos = Equipo.objects.select_related('categoria', 'marca').all()
    if query:
        equipos = equipos.filter(nombre__icontains=query)
    return render(request, 'gimnasio/catalogo.html', {'equipos': equipos, 'query': query})
