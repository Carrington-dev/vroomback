import json
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .mq import RabbitMQ, sender as publisher
from django.http import JsonResponse
from vroomweb.settings import settings

def send_message(request):
    message = ''

    try:
        publisher = RabbitMQ(**settings.RABBITMQ['default'])
        publisher.send_message(
                exchange = "",  
                routing_key = 'letterhead',
                # routing_key = 'user.deleted.1.2.3',
                data = json.dumps({
                    "message": 'Carrington is learning django from views.home'
                })
            )
        message = ' RabbitMQ worked properly'
    except Exception as e:
        print(e)
        message = str(e)
        

    # return render(request, 'send_message.html', {})
    return JsonResponse({
        'message': message
    })