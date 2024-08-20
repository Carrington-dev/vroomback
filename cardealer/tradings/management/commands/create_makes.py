from django.core.management.base import BaseCommand
from tradings.models import  Make
from vroomweb import settings

class Command(BaseCommand):
    help = 'Consumes messages from the specified queue'

    def add_arguments(self, parser):
        pass
        # parser.add_argument('letterhead', type=str, help='The name of the queue to consume messages from')

    def handle(self, *args, **options):
        # queue_name = options['letterhead']
        # print(queue_name)
        with open(f"{settings.BASE_DIR}/makes.txt", ) as f:
            for line in f.readlines():
                Make.objects.get_or_create(name=line.strip())
        
        print('Created All Makes')