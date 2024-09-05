from news.models import Post
from news.mixins import PostListReadMixin
from news.serializers import PostSerializer
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

class PostViewSet(PostListReadMixin):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    model = Post

    @method_decorator(cache_page(60 * 15))  # Cache for 15 minutes
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @method_decorator(cache_page(60 * 15))
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)