from django.core.validators import MinValueValidator
from django.db import models


class Categoria(models.Model):
    """Categoria de equipamiento (ej: Cardio, Fuerza, Funcional)."""
    nombre = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"
        ordering = ['nombre']

    def __str__(self):
        return self.nombre


class Marca(models.Model):
    """Marca fabricante del equipo (ej: Technogym, Rogue)."""
    nombre = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name = "Marca"
        verbose_name_plural = "Marcas"
        ordering = ['nombre']

    def __str__(self):
        return self.nombre


class Equipo(models.Model):
    """Equipo/maquina del catalogo de gimnasio."""
    nombre = models.CharField(max_length=200)
    anio = models.PositiveIntegerField(verbose_name="Ano de incorporacion")
    imagen = models.CharField(
        max_length=255,
        help_text="Ruta relativa dentro de static/, ej: images/gimnasio/rack.svg"
    )
    categoria = models.ForeignKey(
        Categoria, on_delete=models.PROTECT, related_name='equipos'
    )
    marca = models.ForeignKey(
        Marca, on_delete=models.PROTECT, related_name='equipos'
    )
    precio = models.DecimalField(
        max_digits=10, decimal_places=2, default=0,
        validators=[MinValueValidator(0)],
        help_text="Precio del equipo, editable desde Django Admin."
    )

    class Meta:
        verbose_name = "Equipo"
        verbose_name_plural = "Equipos"
        ordering = ['-anio', 'nombre']

    def __str__(self):
        return f"{self.nombre} ({self.anio})"
