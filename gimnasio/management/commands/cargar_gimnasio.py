import json
from pathlib import Path

from django.core.management.base import BaseCommand

from gimnasio.models import Categoria, Marca, Equipo

BASE_DIR = Path(__file__).resolve().parent.parent.parent


class Command(BaseCommand):
    help = "Migra los datos de gimnasio/data/equipos.json hacia la base de datos."

    def handle(self, *args, **options):
        ruta_json = BASE_DIR / 'data' / 'equipos.json'

        if not ruta_json.exists():
            self.stderr.write(self.style.ERROR(f"No se encontro el archivo: {ruta_json}"))
            return

        with open(ruta_json, encoding='utf-8') as archivo:
            equipos = json.load(archivo)

        creados = 0
        for item in equipos:
            categoria_obj, _ = Categoria.objects.get_or_create(nombre=item['categoria'])
            marca_obj, _ = Marca.objects.get_or_create(nombre=item['marca'])

            _, fue_creado = Equipo.objects.get_or_create(
                nombre=item['nombre'],
                defaults={
                    'anio': item['anio'],
                    'imagen': item['imagen'],
                    'categoria': categoria_obj,
                    'marca': marca_obj,
                    'precio': item.get('precio', 0),
                }
            )
            if fue_creado:
                creados += 1

        self.stdout.write(self.style.SUCCESS(
            f"Listo. {creados} equipos nuevos creados (de {len(equipos)} en el JSON)."
        ))
