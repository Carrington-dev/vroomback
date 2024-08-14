from django.core.management.base import BaseCommand
from tradings.mq import  RabbitMQ, sender as publisher
from cardealer.vroomweb import settings

class Command(BaseCommand):
    help = 'Consumes messages from the specified queue'

    def add_arguments(self, parser):
        parser.add_argument('letterhead', type=str, help='The name of the queue to consume messages from')

    def handle(self, *args, **options):
        queue_name = options['letterhead']
        # print(queue_name)
        # Define a callback function to process the received message
        def callback(ch, method, properties, body):
            print(" [x] Received %r" % body)

        # publisher = RabbitMQ(**settings.RABBITMQ['default'])
        publisher.recieve_message()