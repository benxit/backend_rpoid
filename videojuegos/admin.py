from django.contrib import admin
from .models import Genero, Plataforma, Videojuego


@admin.register(Genero)
class GeneroAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')
    search_fields = ('nombre',)


@admin.register(Plataforma)
class PlataformaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')
    search_fields = ('nombre',)


@admin.register(Videojuego)
class VideojuegoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'anio', 'genero', 'plataforma', 'precio')
    list_filter = ('genero', 'plataforma', 'anio')
    search_fields = ('nombre', 'genero__nombre', 'plataforma__nombre')
    autocomplete_fields = ('genero', 'plataforma')
    list_editable = ('precio',)
    ordering = ('-anio',)
