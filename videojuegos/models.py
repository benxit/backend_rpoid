from django.core.validators import MinValueValidator
from django.db import models


class Genero(models.Model):
    """Categoria/genero de un videojuego (ej: RPG, Carreras)."""
    nombre = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name = "Genero"
        verbose_name_plural = "Generos"
        ordering = ['nombre']

    def __str__(self):
        return self.nombre


class Plataforma(models.Model):
    """Plataforma en la que esta disponible el videojuego (ej: PC, PS5)."""
    nombre = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name = "Plataforma"
        verbose_name_plural = "Plataformas"
        ordering = ['nombre']

    def __str__(self):
        return self.nombre


class Videojuego(models.Model):
    """Videojuego del catalogo."""
    nombre = models.CharField(max_length=200)
    anio = models.PositiveIntegerField(verbose_name="Ano")
    imagen = models.CharField(
        max_length=255,
        help_text="Ruta relativa dentro de static/, ej: images/videojuegos/gta5.jpg"
    )
    genero = models.ForeignKey(
        Genero, on_delete=models.PROTECT, related_name='videojuegos'
    )
    plataforma = models.ForeignKey(
        Plataforma, on_delete=models.PROTECT, related_name='videojuegos'
    )
    precio = models.DecimalField(
        max_digits=10, decimal_places=2, default=0,
        validators=[MinValueValidator(0)],
        help_text="Precio de venta, editable desde Django Admin."
    )

    class Meta:
        verbose_name = "Videojuego"
        verbose_name_plural = "Videojuegos"
        ordering = ['-anio', 'nombre']

    def __str__(self):
        return f"{self.nombre} ({self.anio})"
