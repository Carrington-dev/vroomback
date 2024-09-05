from django.contrib import admin
from news.actions import duplicate_post
from news.models import Image, Post

class ImageInline(admin.TabularInline):
    model = Image
    extra = 0


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = [ 'id' ,'author' ,'title' ,  'short_description' ,'content' ,'image']
    inlines = [ ImageInline ]
    actions = [ duplicate_post ]

