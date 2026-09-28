import json
from pathlib import Path

from django.core.management.base import BaseCommand

from peliculas.models import Genero, Director, Pelicula

BASE_DIR = Path(__file__).resolve().parent.parent.parent


class Command(BaseCommand):
    help = "Migra los datos de peliculas/data/peliculas.json hacia la base de datos."

    def handle(self, *args, **options):
        ruta_json = BASE_DIR / 'data' / 'peliculas.json'

        if not ruta_json.exists():
            self.stderr.write(self.style.ERROR(f"No se encontro el archivo: {ruta_json}"))
            return

        with open(ruta_json, encoding='utf-8') as archivo:
            peliculas = json.load(archivo)

        creadas = 0
        for item in peliculas:
            genero_obj, _ = Genero.objects.get_or_create(nombre=item['genero'])
            director_obj, _ = Director.objects.get_or_create(nombre=item['director'])

            _, fue_creada = Pelicula.objects.get_or_create(
                titulo=item['titulo'],
                defaults={
                    'anio': item['anio'],
                    'imagen': item['imagen'],
                    'genero': genero_obj,
                    'director': director_obj,
                    'precio': item.get('precio', 0),
                }
            )
            if fue_creada:
                creadas += 1

        self.stdout.write(self.style.SUCCESS(
            f"Listo. {creadas} peliculas nuevas creadas (de {len(peliculas)} en el JSON)."
        ))
