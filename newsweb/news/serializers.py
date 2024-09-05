from news.models import Image, Post
from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'username', 'first_name', 'last_name', )

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = [ 'id' , 'photo']

class PostSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True, read_only=True)
    author = UserSerializer(read_only=True)
    
    class Meta:
        model = Post
        fields = [ 'id' ,'author' ,'title' ,  'short_description' ,'content' , 'created_at','image', 'images',]