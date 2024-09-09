from rest_framework import serializers
from news.models import Image, Post, Category, Tag
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'username', 'first_name', 'last_name', )


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = [ 'id' , 'name']


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = [ 'id' , 'photo']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [ 'id' , 'name', 'post_count' ]


class NewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = [ 'id' ,'author', 'category' , 'title' , 'slug', 'created_at',]


class PostSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True, read_only=True)
    author = UserSerializer(read_only=True)
    category = CategorySerializer(read_only=True)
    previous_post = NewSerializer()
    next_post = NewSerializer()

    # This would work as well

    # previous_post = serializers.SerializerMethodField()
    # next_post = serializers.SerializerMethodField()
    
    class Meta:
        model = Post
        fields = [ 'id' ,'author', 'category' , 'title' , 'slug',  'short_description' ,'content' , 'created_at','image', 'images', 'previous_post', 'next_post']


    # def get_previous_post(self, obj):
    #     # Get the previous post based on the created_at field
    #     previous_post = Post.objects.filter(created_at__lt=obj.created_at).order_by('-created_at').first()
    #     return previous_post.id if previous_post else None

    # def get_next_post(self, obj):
    #     # Get the next post based on the created_at field
    #     next_post = Post.objects.filter(created_at__gt=obj.created_at).order_by('created_at').first()
    #     return next_post.id if next_post else None