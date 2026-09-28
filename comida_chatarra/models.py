from django.core.validators import MinValueValidator
from django.db import models


class Categoria(models.Model):
    """Categoria del producto (ej: Papas fritas, Hamburguesas, Dulces)."""
    nombre = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"
        ordering = ['nombre']

    def __str__(self):
        return self.nombre


class Marca(models.Model):
    """Marca del producto (ej: Lays, McDonald's, Coca-Cola)."""
    nombre = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name = "Marca"
        verbose_name_plural = "Marcas"
        ordering = ['nombre']

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    """Producto del catalogo de comida chatarra."""
    nombre = models.CharField(max_length=200)
    anio = models.PositiveIntegerField(verbose_name="Ano de lanzamiento")
    imagen = models.CharField(
        max_length=255,
        help_text="Ruta relativa dentro de static/, ej: images/comida_chatarra/papas.svg"
    )
    categoria = models.ForeignKey(
        Categoria, on_delete=models.PROTECT, related_name='productos'
    )
    marca = models.ForeignKey(
        Marca, on_delete=models.PROTECT, related_name='productos'
    )
    precio = models.DecimalField(
        max_digits=10, decimal_places=2, default=0,
        validators=[MinValueValidator(0)],
        help_text="Precio de venta, editable desde Django Admin."
    )

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"
        ordering = ['-anio', 'nombre']

    def __str__(self):
        return f"{self.nombre} ({self.anio})"
