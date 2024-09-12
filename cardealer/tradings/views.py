import json
import datetime
from django.shortcuts import render
from tradings.pagination import CustomBrandPagination
from django_filters import rest_framework as filters

from security.models import User
from tradings.filters import VehicleFilter, VehicleModelFilter
from tradings.mixins import VehicleMixin
from tradings.seriliazers import CitySerializer, CountrySerializer, EnquirySerializer, MakeSerializer, CarModelSerializer, MakeVehiclesSerializer, StateSerializer, VariantSerializer, VehicleSerializer, VehicleSerializerByUser
from tradings.models import CarModel, City, Country, Enquiry, Make, State, Variant, Vehicle
# from .mq import RabbitMQ
from django.http import JsonResponse
from vroomweb import settings
from rest_framework.viewsets import ModelViewSet
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Count

class MakeVehiclesViewSet(ModelViewSet):
    serializer_class = MakeVehiclesSerializer
    queryset = Make.objects.all()
    pagination_class = CustomBrandPagination


    @method_decorator(cache_page(60 * 15))  # Cache for 15 minutes
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @method_decorator(cache_page(60 * 15))
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

class MakeViewSet(ModelViewSet):
    serializer_class = MakeSerializer
    queryset = Make.objects.all().annotate(num_vehicles=Count('make_vehicles')).order_by('-num_vehicles')
    

    @method_decorator(cache_page(60 * 15))  # Cache for 15 minutes
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @method_decorator(cache_page(60 * 15))
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

class StateViewSet(ModelViewSet):
    serializer_class = StateSerializer
    queryset = State.objects.all()

    @method_decorator(cache_page(60 * 15))  # Cache for 15 minutes
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @method_decorator(cache_page(60 * 15))
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

class CityViewSet(ModelViewSet):
    serializer_class = CitySerializer
    queryset = City.objects.all()

    @method_decorator(cache_page(60 * 15))  # Cache for 15 minutes
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @method_decorator(cache_page(60 * 15))
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

class CountryViewSet(ModelViewSet):
    serializer_class = CountrySerializer
    queryset = Country.objects.all()

    @method_decorator(cache_page(60 * 15))  # Cache for 15 minutes
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @method_decorator(cache_page(60 * 15))
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)


class VehicleViewSet(VehicleMixin):
    serializer_class = VehicleSerializer
    queryset = Vehicle.objects.filter(status='published')
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('make_id', "city_id", 'condition', "user_id", "year", "type")
    filterset_class = VehicleFilter


    @method_decorator(cache_page(60 * 15))  # Cache for 15 minutes
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @method_decorator(cache_page(60 * 15))
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
    
class FilteredVehicleViewSet(VehicleMixin):
    serializer_class = VehicleSerializer
    queryset = Vehicle.objects.filter(status='published')
    filterset_class = VehicleModelFilter
    # filterset_fields = ['title', 'model_name', 'model_make_name']


    @method_decorator(cache_page(60 * 15))  # Cache for 15 minutes
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @method_decorator(cache_page(60 * 15))
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

class CarModelViewSet(ModelViewSet):
    serializer_class = CarModelSerializer
    queryset = CarModel.objects.all()

    @method_decorator(cache_page(60 * 15))  # Cache for 15 minutes
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @method_decorator(cache_page(60 * 15))
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

class UserVehiclesModelViewSet(VehicleMixin):
    serializer_class = VehicleSerializerByUser
    queryset = User.objects.all()

    @method_decorator(cache_page(60 * 15))  # Cache for 15 minutes
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @method_decorator(cache_page(60 * 15))
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

class VariantModelViewSet(VehicleMixin):
    serializer_class = VariantSerializer
    queryset = Variant.objects.all()

    @method_decorator(cache_page(60 * 15))  # Cache for 15 minutes
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @method_decorator(cache_page(60 * 15))
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)



class EnquiryViewSet(ModelViewSet):
    serializer_class = EnquirySerializer
    queryset = Enquiry.objects.all()

    @method_decorator(cache_page(60 * 15))  # Cache for 15 minutes
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @method_decorator(cache_page(60 * 15))
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)



"""
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
"""