import django_filters
from .models import Vehicle

class VehicleModelFilter(django_filters.FilterSet):
    class Meta:
        model = Vehicle
        fields = {
            'title': ['icontains'],
            'colour': ['exact', 'icontains'],
            # add more fields and filter types as needed
        }
