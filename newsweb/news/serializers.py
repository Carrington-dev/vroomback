from news.models import Image, Post
from rest_framework import serializers


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = [ 'id' , 'photo']

class PostSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True, read_only=True)
    
    class Meta:
        model = Post
        fields = [ 'id' ,'author' ,'title' , 'images', 'short_description' ,'content' ,'image']