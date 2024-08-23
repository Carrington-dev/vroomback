import django_filters
from django_filters import rest_framework as filters

from .models import Vehicle

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
