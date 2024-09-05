from news.models import Post
from django.shortcuts import render
from rest_framework import viewsets
from news.mixins import PostCreateReadMixin
from news.serializers import PostSerializer

class PostViewSet(PostCreateReadMixin):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    model = Post