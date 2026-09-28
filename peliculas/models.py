from django.core.validators import MinValueValidator
from django.db import models


class Genero(models.Model):
    """Categoria/genero de una pelicula (ej: Ciencia ficcion, Drama)."""
    nombre = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name = "Genero"
        verbose_name_plural = "Generos"
        ordering = ['nombre']

    def __str__(self):
        return self.nombre


class Director(models.Model):
    """Director/a a cargo de una o varias peliculas."""
    nombre = models.CharField(max_length=150, unique=True)

    class Meta:
        verbose_name = "Director"
        verbose_name_plural = "Directores"
        ordering = ['nombre']

    def __str__(self):
        return self.nombre


class Pelicula(models.Model):
    """Pelicula del catalogo."""
    titulo = models.CharField(max_length=200)
    anio = models.PositiveIntegerField(verbose_name="Ano")
    imagen = models.CharField(
        max_length=255,
        help_text="Ruta relativa dentro de static/, ej: images/peliculas/dune.jpg"
    )
    genero = models.ForeignKey(
        Genero, on_delete=models.PROTECT, related_name='peliculas'
    )
    director = models.ForeignKey(
        Director, on_delete=models.PROTECT, related_name='peliculas'
    )
    precio = models.DecimalField(
        max_digits=10, decimal_places=2, default=0,
        validators=[MinValueValidator(0)],
        help_text="Precio de arriendo/venta, editable desde Django Admin."
    )

    class Meta:
        verbose_name = "Pelicula"
        verbose_name_plural = "Peliculas"
        ordering = ['-anio', 'titulo']

    def __str__(self):
        return f"{self.titulo} ({self.anio})"
