from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

def inicio(request):
    return redirect('videojuegos:inicio')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('videojuegos/', include('videojuegos.urls')),
    path('peliculas/', include('peliculas.urls')),
    path('gimnasio/', include('gimnasio.urls')),
    path('comida-chatarra/', include('comida_chatarra.urls')),
    path('', inicio),
]
