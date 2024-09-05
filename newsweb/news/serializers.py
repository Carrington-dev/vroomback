from news.models import Post
from rest_framework import serializers

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = [ 'id' ,'author' ,'title' ,'short_description' ,'content' ,'image']