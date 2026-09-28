from django.shortcuts import render

from .models import Producto


def inicio(request):
    return render(request, 'comida_chatarra/inicio.html')


def catalogo(request):
    query = request.GET.get('q', '').strip()
    productos = Producto.objects.select_related('categoria', 'marca').all()
    if query:
        productos = productos.filter(nombre__icontains=query)
    return render(request, 'comida_chatarra/catalogo.html', {'productos': productos, 'query': query})
