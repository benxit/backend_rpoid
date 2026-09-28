from django.contrib import admin
from .models import Categoria, Marca, Producto


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')
    search_fields = ('nombre',)


@admin.register(Marca)
class MarcaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')
    search_fields = ('nombre',)


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'categoria', 'marca', 'anio', 'precio')
    list_filter = ('categoria', 'marca', 'anio')
    search_fields = ('nombre', 'categoria__nombre', 'marca__nombre')
    autocomplete_fields = ('categoria', 'marca')
    list_editable = ('precio',)
    ordering = ('-anio',)
