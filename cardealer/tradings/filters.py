from uuid import UUID
from django.shortcuts import get_object_or_404
import django_filters
from django_filters import rest_framework as filters
from .models import City, Make, Vehicle
from django.db.models import Q

class VehicleModelFilter(filters.FilterSet):
    class Meta:
        model = Vehicle
        fields = {
            'title': ['icontains'],
            'colour': ['exact', 'icontains'],
            'make_id': ['exact', ],
            'year': ['exact', ],
            # add more fields and filter types as needed
        }

# filters.py


class VehicleFilter(filters.FilterSet):
    brands = filters.CharFilter(method='filter_by_brands')
    cities = filters.CharFilter(method='filter_by_cities')
    types = filters.CharFilter(method='filter_by_body_types')
    # years = filters.CharFilter(method='filter_by_years')
    search = django_filters.CharFilter(method='filter_by_all_fields')

    price_gt = filters.NumberFilter(field_name="price", lookup_expr='gte')
    price_lt = filters.NumberFilter(field_name="price", lookup_expr='lte')

    class Meta:
        model = Vehicle
        fields = {
            # 'title': ['icontains'],
            # 'colour': ['exact', 'icontains'],
            'model_id': ['exact', ],
            'make_id': ['exact', ],
            # 'year': ['exact', ],
            "city_id": [ 'exact'],
            'condition': [ 'exact'],
            "user_id": [ 'exact'],
            "type": [ 'exact'],
            'year': [ 'lte', 'gte'], 
            'mileage': [ 'lte', 'gte'], 
            # 'price': [ 'lte'], 
            # 'price_lt': [ 'lt'],

        # add more fields and filter types as needed
        }

    def filter_by_brands(self, queryset, name, value):
        # Split the incoming string by commas to create a list of authors
        make_list = list(map(str, value.split(',')))
        # Filter the queryset by this list
        make_list = [ get_object_or_404(Make, pk=id) for id in make_list]
        return queryset.filter(make__in=make_list)

    def filter_by_cities(self, queryset, name, value):
        # Split the incoming string by commas to create a list of authors
        city_list = list(map(str, value.split(',')))
        # Filter the queryset by this list
        city_list = [  get_object_or_404(City, pk=id) for id in city_list]
        # print(city_list)
        return queryset.filter(city__in=city_list)
    
    def filter_by_body_types(self, queryset, name, value):
        body_type_list = list(map(str, value.split(',')))
        return queryset.filter(type__in=body_type_list)

    # def filter_by_years(self, queryset, name, value):
    #     year_list = list(map(str, value.split(',')))
    #     return queryset.filter(year__in=year_list)

    def filter_by_all_fields(self, queryset, name, value):
        return queryset.filter(
            Q(title__icontains=value) | Q(make__name__icontains=value)
        )