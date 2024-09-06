from .models import Post
from django.db.models import Q
from django_filters import rest_framework as filters

class PostModelFilter(filters.FilterSet):
    class Meta:
        model = Post
        fields = {
            'title': ['icontains'],
            'category_id': ['exact', ],
            # add more fields and filter types as needed
        }