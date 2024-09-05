from django.contrib import admin
from news.models import Image, Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = [ 'id' ,'author' ,'title' ,  'short_description' ,'content' ,'image']


