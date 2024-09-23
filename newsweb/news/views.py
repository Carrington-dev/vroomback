from news.models import Category, Contact, Post, Tag
from news.mixins import PostListReadMixin
from news.serializers import CategorySerializer, ContactSerializer, PostSerializer, TagSerializer
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django_filters import rest_framework as filters
from rest_framework import viewsets

class PostViewSet(PostListReadMixin):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    model = Post
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('category_id', )

    @method_decorator(cache_page(60 * 15))  # Cache for 15 minutes
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @method_decorator(cache_page(60 * 15))
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
    
class CategoryViewSet(PostListReadMixin):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    model = Category

    @method_decorator(cache_page(60 * 15))  # Cache for 15 minutes
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @method_decorator(cache_page(60 * 15))
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
    
class TagViewSet(PostListReadMixin):
    serializer_class = TagSerializer
    queryset = Tag.objects.all()
    model = Tag

    @method_decorator(cache_page(60 * 15))  # Cache for 15 minutes
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @method_decorator(cache_page(60 * 15))
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
    
class ContactViewSet(viewsets.ModelViewSet):
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()
    model = Contact

    @method_decorator(cache_page(60 * 15))  # Cache for 15 minutes
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @method_decorator(cache_page(60 * 15))
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)