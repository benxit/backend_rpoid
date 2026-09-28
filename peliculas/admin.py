from django.contrib import admin
from .models import Genero, Director, Pelicula


@admin.register(Genero)
class GeneroAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')
    search_fields = ('nombre',)


@admin.register(Director)
class DirectorAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')
    search_fields = ('nombre',)


@admin.register(Pelicula)
class PeliculaAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'anio', 'genero', 'director', 'precio')
    list_filter = ('genero', 'director', 'anio')
    search_fields = ('titulo', 'director__nombre', 'genero__nombre')
    autocomplete_fields = ('genero', 'director')
    list_editable = ('precio',)
    ordering = ('-anio',)
