from news.models import Post
from news.mixins import PostListReadMixin
from news.serializers import PostSerializer

class PostViewSet(PostListReadMixin):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    model = Post