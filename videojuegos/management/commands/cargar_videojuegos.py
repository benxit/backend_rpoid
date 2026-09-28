import json
from pathlib import Path

from django.core.management.base import BaseCommand

from videojuegos.models import Genero, Plataforma, Videojuego

BASE_DIR = Path(__file__).resolve().parent.parent.parent


class Command(BaseCommand):
    help = "Migra los datos de videojuegos/data/juegos.json hacia la base de datos."

    def handle(self, *args, **options):
        ruta_json = BASE_DIR / 'data' / 'juegos.json'

        if not ruta_json.exists():
            self.stderr.write(self.style.ERROR(f"No se encontro el archivo: {ruta_json}"))
            return

        with open(ruta_json, encoding='utf-8') as archivo:
            juegos = json.load(archivo)

        creados = 0
        for item in juegos:
            genero_obj, _ = Genero.objects.get_or_create(nombre=item['genero'])
            plataforma_obj, _ = Plataforma.objects.get_or_create(nombre=item['plataforma'])

            _, fue_creado = Videojuego.objects.get_or_create(
                nombre=item['nombre'],
                defaults={
                    'anio': item['anio'],
                    'imagen': item['imagen'],
                    'genero': genero_obj,
                    'plataforma': plataforma_obj,
                    'precio': item.get('precio', 0),
                }
            )
            if fue_creado:
                creados += 1

        self.stdout.write(self.style.SUCCESS(
            f"Listo. {creados} videojuegos nuevos creados (de {len(juegos)} en el JSON)."
        ))
