import uuid
from django.db import models
from vroomweb import settings
from django_resized import ResizedImageField
from django.template.defaultfilters import slugify
# from news.fields import OrderField


STATUS = (
    ('draft', 'Draft'),
    ('published', 'Published'),
)
class News(models.Model):
    id = models.UUIDField( 
         primary_key = True, 
         default = uuid.uuid4, 
         editable = False)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="news")
    title = models.CharField(max_length=500)
    short_description = models.TextField()
    content = models.TextField()
    slug = models.SlugField(max_length=250, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=100, choices=STATUS, default="draft")
    image = ResizedImageField(size=[1024, 768], crop=['middle', 'center'], upload_to='news/thumbnails')

    def __str__(self):
        return f"{self.title} *{self.id}"

    def __unicode__(self):
        return f"{self.title} *{self.id}"
