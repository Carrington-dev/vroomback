import json
import datetime
from django.shortcuts import render

from tradings.mixins import VehicleMixin
from tradings.seriliazers import CitySerializer, CountrySerializer, MakeSerializer, ModelSerializer, StateSerializer, VehicleSerializer
from tradings.models import CarModel, City, Country, Make, State, Vehicle
from .mq import RabbitMQ
from django.http import JsonResponse
from vroomweb.settings import settings
from rest_framework.viewsets import ModelViewSet


class MakeViewSet(ModelViewSet):
    serializer_class = MakeSerializer
    queryset = Make.objects.all()

class StateViewSet(ModelViewSet):
    serializer_class = StateSerializer
    queryset = State.objects.all()

class CityViewSet(ModelViewSet):
    serializer_class = CitySerializer
    queryset = City.objects.all()

class CountryViewSet(ModelViewSet):
    serializer_class = CountrySerializer
    queryset = Country.objects.all()



class VehicleViewSet(VehicleMixin):
    serializer_class = VehicleSerializer
    queryset = Vehicle.objects.filter(status='published')



class CarModelViewSet(ModelViewSet):
    serializer_class = ModelSerializer
    queryset = CarModel.objects.all()






def send_message(request):
    message = ''

    try:
        publisher = RabbitMQ(**settings.RABBITMQ['default'])
        publisher.send_message(
                exchange = "",  
                routing_key = 'letterhead',
                # routing_key = 'user.deleted.1.2.3',
                data = json.dumps({
                    "message": 'Carrington is learning django from views.home',
                    'time_sent': str(datetime.datetime.now())
                })
            )
        message = ' RabbitMQ worked properly'
    except Exception as e:
        # print(e)
        message = str(e)
        

    # return render(request, 'send_message.html', {})
    return JsonResponse({
        'message': message,
        'time_sent': str(datetime.datetime.now())
    })