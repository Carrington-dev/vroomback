from django.shortcuts import render
from rest_framework import viewsets
from news.models import Post
from news.serializers import PostSerializer

class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    model = Post