import uuid
from django.db import models
from news.utils import MAX_OBJECTS, user_directory_path, user_directory_path_image
from vroomweb import settings
from django_resized import ResizedImageField
from django.template.defaultfilters import slugify
# from news.fields import OrderField


STATUS = (
    ('draft', 'Draft'),
    ('published', 'Published'),
)

class Category(models.Model):
    id = models.UUIDField( 
         primary_key = True, 
         default = uuid.uuid4, 
         editable = False)
    name = models.CharField(max_length=500)

    def post_count(self):
        return self.posts.count()

    def __str__(self):
        return f"{self.name} *{self.id}"

    def __unicode__(self):
        return f"{self.name} *{self.id}"
    
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
    
class Tag(models.Model):
    id = models.UUIDField( 
         primary_key = True, 
         default = uuid.uuid4, 
         editable = False)
    name = models.CharField(max_length=500)

    def __str__(self):
        return f"{self.name} *{self.id}"

    def __unicode__(self):
        return f"{self.name} *{self.id}"


class Post(models.Model):
    id = models.UUIDField( 
         primary_key = True, 
         default = uuid.uuid4, 
         editable = False)
    category = models.ForeignKey('Category', related_name='posts', on_delete=models.CASCADE, blank=True, null=True)
    tags = models.ManyToManyField('Tag', related_name='posts', blank=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="news")
    title = models.CharField(max_length=500)
    short_description = models.TextField()
    content = models.TextField()
    slug = models.SlugField(max_length=250, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=100, choices=STATUS, default="draft")
    image = ResizedImageField(size=[1224, 768], crop=['middle', 'center'], default='post/post.jpg', upload_to=user_directory_path, ) #upload_to='news/thumbnails')

    def __str__(self):
        return f"{self.title} *{self.id}"

    def __unicode__(self):
        return f"{self.title} *{self.id}"
    
    def save(self, *args, **kwargs):
        self.slug = slugify(f"{self.title}-{self.id}")
        return super().save(*args, **kwargs)
    
    def  previous_post(self):
        return Post.objects.filter(created_at__lt=self.created_at).order_by('-created_at').first()
    

    def next_post(self):
        return Post.objects.filter(created_at__gt=self.created_at).order_by('created_at').first()

    
    class Meta:
        
        ordering = ['-created_at', 'title']


class Image(models.Model):
    id = models.UUIDField( 
         primary_key = True, 
         default = uuid.uuid4, 
         editable = False)
    post = models.ForeignKey(Post, related_name="images",  on_delete=models.CASCADE)
    photo = ResizedImageField(size=[882, 484], crop=['middle', 'center'],  upload_to=user_directory_path_image)

    def __str__(self):
        return f"{self.post.title}"

    def __unicode__(self):
        return f"{self.post.title}"
    
    def has_add_permission(self, request):
        if self.post.images.objects.count() >= MAX_OBJECTS:
            return False
        return super().has_add_permission(request)
    

class Contact(models.Model):
    id = models.UUIDField( 
         primary_key = True, 
         default = uuid.uuid4, 
         editable = False)
   
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    subject = models.CharField(max_length=300)
    phone = models.CharField(max_length=30)
    notes = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.email}"

    def __unicode__(self):
        return f"{self.email}"
    