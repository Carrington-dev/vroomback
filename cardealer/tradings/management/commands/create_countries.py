from django.core.management.base import BaseCommand
from tradings.utils import COUNTRIES
from tradings.models import  City, Country, Make
from cardealer.vroomweb import settings

class Command(BaseCommand):
    help = 'Consumes messages from the specified queue'

    def add_arguments(self, parser):
        parser.add_argument('letterhead', type=str, help='The name of the queue to consume messages from')

    def handle(self, *args, **options):
        queue_name = options['letterhead']
        # print(queue_name)
        
        for line in COUNTRIES:
            Country.objects.get_or_create(name=line[0])
        
        print('Created All Countries')