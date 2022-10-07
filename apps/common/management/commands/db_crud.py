import json
import os

from django.contrib.gis.geos import MultiPolygon, Polygon
from django.core.cache import cache
from django.core.management import BaseCommand

from common.models import Region, Country
from locust.settings import BASE_DIR


def regions():
    try:
        regions = json.load(open(os.path.join(BASE_DIR, 'regions.json')))
        uzb = Country.objects.get(alpha_two_code='UZ')
        for region in regions['features']:
            polygons = []
            for i in region['geometry']['coordinates']:
                polygons.append(Polygon(i[0]))
            try:
                instance = Region.objects.get(pk=region['id'])
                instance.country = uzb
                instance.name_uz = region['name_uz']
                instance.name_en = region['name_en']
                instance.name_ru = region['name_ru']
                instance.geometry = MultiPolygon(polygons)
                instance.save()
                print(f'{instance.name_uz} is successfully updated.')
            except:
                Region.objects.create(
                    id=region['id'],
                    country=uzb,
                    name_uz=region['name_uz'],
                    name_en=region['name_en'],
                    name_ru=region['name_ru'],
                    geometry=MultiPolygon(polygons),
                )
                print(f'{instance.name_uz} is successfully created.')
    except Exception as e:
        print(e)


class Command(BaseCommand):
    help = 'It will seed database automatically with initial data'

    def handle(self, *args, **options):
        regions()
        # cache.clear()
