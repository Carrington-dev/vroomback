import uuid
from datetime import datetime
from django.db import models
from django.dispatch import receiver
from tradings.helpers import user_directory_path, user_directory_path_image
from django_resized import ResizedImageField
from django.template.defaultfilters import slugify
from django.db.models.signals import post_save, pre_delete
from tradings.abstracts import EnginePerformanceTemplate, KeyFeatureTemplate
from tradings.utils import CONDITION, DEFAULT_VIDEO_LINK, MAX_OBJECTS, FUEL_TYPES, COUNTRIES, IMAGE_CLASSES, STATUS, TYPE_OF_VEHICLE, YEARS_TO_CHOOSE
from vroomweb import settings
from django.core.validators import FileExtensionValidator

class Country(models.Model):
    id        = models.UUIDField( 
                    primary_key = True, 
                    default = uuid.uuid4, 
                    editable = False)
    name       = models.CharField(max_length=254, unique=True, choices=COUNTRIES, default="ZA")

    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    # created_at = models.DateTimeField(default=datetime.now, blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}" 

    def __unicode__(self):
        return f"{self.name}"
    
    class Meta:
        verbose_name = 'Country'
        verbose_name_plural = 'Countries'
        ordering = [ 'name' ]
    
class Make(models.Model):
    id      = models.UUIDField( 
                primary_key = True, 
                default = uuid.uuid4, 
                editable = False)
    name    = models.CharField(max_length=254, unique=True)
    icon       = models.FileField(upload_to="icons/%Y/%m/%d/", default="vehicle/tesla.svg", validators=[FileExtensionValidator(['svg'])])
    image       = models.FileField(upload_to="photos/",  default="vehicle/car_image.svg", validators=[FileExtensionValidator(['svg'])])
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    def vehicle_count(self):
        return self.make_vehicles.count()

    def __str__(self):
        return f"{self.name}" 

    def __unicode__(self):
        return f"{self.name}"
    
    class Meta:
        verbose_name = 'Make'
        verbose_name_plural = 'Makes'
        ordering = [ 'name' ]
    
class City(models.Model):
    id      = models.UUIDField( 
                primary_key = True, 
                default = uuid.uuid4, 
                editable = False)
    name    = models.CharField(max_length=254, unique=True)
    country    = models.ForeignKey(Country, related_name="cities", on_delete=models.SET_NULL, null=True, blank=True)
    state    = models.ForeignKey("State", related_name="cities", on_delete=models.SET_NULL, null=True, blank=True)


    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    def vehicle_count(self):
        return self.city_vehicles.count()

    def __str__(self):
        return f"{self.name}" 

    def __unicode__(self):
        return f"{self.name}"
    
    class Meta:
        verbose_name = 'City'
        verbose_name_plural = 'Cities'
        ordering = [ 'name' ]
    
class State(models.Model):
    id  = models.UUIDField( 
            primary_key = True, 
            default = uuid.uuid4, 
            editable = False)
    name = models.CharField(max_length=254, unique=True)
    country    = models.ForeignKey(Country, related_name="states", on_delete=models.SET_NULL, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}" 
    
    def vehicle_count(self):
        return self.state_vehicles.count()

    def __unicode__(self):
        return f"{self.name}"
    
    class Meta:
        ordering = [ 'name' ]
    
class Color(models.Model):
    id          = models.UUIDField( 
                    primary_key = True, 
                    default = uuid.uuid4, 
                    editable = False)
    name        = models.CharField(max_length=254, unique=True)
    hexadecimal = models.CharField(max_length=254, unique=True)


    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}" 

    def __unicode__(self):
        return f"{self.name}"
    
class CarModel(models.Model):
    id      = models.UUIDField( 
                primary_key = True, 
                default = uuid.uuid4, 
                editable = False)
    name    = models.CharField(max_length=254, unique=True)
    make    = models.ForeignKey(Make, related_name="models", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}" 

    def __unicode__(self):
        return f"{self.name}"
    
    class Meta:
        verbose_name = 'Model'
        verbose_name_plural = 'Models'
        ordering = [ 'name' ]

    def vehicle_count(self):
        return self.vehicles.count()

class Variant(models.Model):
    id      = models.UUIDField( 
                primary_key = True, 
                default = uuid.uuid4, 
                editable = False)
    name    = models.CharField(max_length=254, unique=True)
    model    = models.ForeignKey(CarModel, related_name="variants", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}" 

    def __unicode__(self):
        return f"{self.name}"
    
    class Meta:
        verbose_name = 'Variant'
        verbose_name_plural = 'Variants'
        ordering = [ 'name' ]

class Vehicle(models.Model):
    id                  = models.UUIDField( 
                            primary_key = True, 
                            default = uuid.uuid4, 
                            editable = False)
    user                = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="vehicles", on_delete=models.CASCADE)
    title               = models.CharField(max_length=254)
    model               = models.ForeignKey(CarModel, related_name="vehicles", on_delete=models.CASCADE)
    variant             = models.ForeignKey(Variant, related_name="variant", on_delete=models.CASCADE)
    make                = models.ForeignKey(Make, related_name="make_vehicles", on_delete=models.CASCADE)
    state               = models.ForeignKey(State, related_name="state_vehicles", on_delete=models.CASCADE)
    city                = models.ForeignKey(City, related_name="city_vehicles", on_delete=models.CASCADE)
    year                = models.IntegerField(('year'), choices=YEARS_TO_CHOOSE, default=2020, )
    price               = models.IntegerField(default=200000)
    mileage             = models.IntegerField(default=0)
    engine_capacity     = models.IntegerField(default=0)
    video_url           = models.URLField(default=DEFAULT_VIDEO_LINK)
    condition           = models.CharField(max_length=100, choices=CONDITION, default='new')
    colour              = models.CharField(max_length=100, default='White')
    top_speed           = models.IntegerField(default=200)
    stock               = models.IntegerField(default=1)
    horse_power         = models.IntegerField(default=200)
    photo               = ResizedImageField(size=[882, 484], crop=['middle', 'center'], default='vehicle/car.jpg', upload_to=user_directory_path)
    airbag_quantity     = models.IntegerField(default=5)
    gears               = models.IntegerField(default=4)
    description         = models.TextField(blank=True, null=True)
    short_description   = models.CharField(max_length=500, blank=True, null=True)
    type                = models.CharField(choices=TYPE_OF_VEHICLE, max_length=100, default='sedan')
    status              = models.CharField(choices=STATUS, max_length=100, default='draft')
    slug                = models.SlugField(max_length=250, default=uuid.uuid4, unique=True)
    created_at          = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at          = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return f"{self.title}"

    def __unicode__(self):
        return f"{self.title}"
    
    def save(self, *args, **kwargs):
        self.slug = slugify(f"{self.title}-{self.id}")
        return super().save(*args, **kwargs)
    
    def interior_images(self):
        return self.images.filter(side="interior")
    
    def exterior_images(self):
        return self.images.filter(side="exterior")
    
    class Meta:
        ordering = [ '-created_at' ]

class VehicleOtherFeatures(EnginePerformanceTemplate):
    id = models.UUIDField( 
         primary_key = True, 
         default = uuid.uuid4, 
         editable = False)
    vehicle = models.OneToOneField(Vehicle, related_name='other_features', on_delete=models.CASCADE)
    
    
    def __str__(self):
        return f"{self.vehicle.title}"

    def __unicode__(self):
        return f"{self.vehicle.title}"

class VehicleKeyFeatures(KeyFeatureTemplate):
    id = models.UUIDField( 
         primary_key = True, 
         default = uuid.uuid4, 
         editable = False)
    vehicle = models.OneToOneField(Vehicle, related_name='key_features', on_delete=models.CASCADE)
    
    
    def __str__(self):
        return f"{self.vehicle.title}"

    def __unicode__(self):
        return f"{self.vehicle.title}"

    

class Image(models.Model):
    id = models.UUIDField( 
         primary_key = True, 
         default = uuid.uuid4, 
         editable = False)
    vehicle = models.ForeignKey(Vehicle, related_name="images", on_delete=models.CASCADE)
    color = models.ForeignKey(Color, related_name="images", on_delete=models.CASCADE)
    side = models.CharField(max_length=300, choices=IMAGE_CLASSES, default="interior")
    photo = ResizedImageField(size=[882, 484], crop=['middle', 'center'],  upload_to=user_directory_path_image)

    def __str__(self):
        return f"{self.vehicle.title}"

    def __unicode__(self):
        return f"{self.vehicle.title}"
    
    def has_add_permission(self, request):
        if self.vehicle.images.objects.count() >= MAX_OBJECTS:
            return False
        return super().has_add_permission(request)
        # if self.model.objects.count() >= MAX_OBJECTS:
        #     return False
        # return super().has_add_permission(request)
    
# Create Vehicle Other Features For This Car on Vehicle creation

@receiver(post_save, sender=Vehicle) 
def create_other_features(sender, instance, created, **kwargs):
    if created:
        VehicleOtherFeatures.objects.create(vehicle=instance, id=instance.id)
  
@receiver(post_save, sender=Vehicle) 
def save_other_features(sender, instance, **kwargs):
        instance.other_features.save()

# Create Vehicle Key Features For This Car on Vehicle creation

@receiver(post_save, sender=Vehicle) 
def create_key_features(sender, instance, created, **kwargs):
    if created:
        VehicleKeyFeatures.objects.create(vehicle=instance, id=instance.id)
  
@receiver(post_save, sender=Vehicle) 
def save_key_features(sender, instance, **kwargs):
        instance.key_features.save()


class Enquiry(models.Model):
    id = models.UUIDField( 
         primary_key = True, 
         default = uuid.uuid4, 
         editable = False)
    vehicle =  models.ForeignKey(Vehicle, on_delete=models.CASCADE, related_name="inquires")
    full_name = models.CharField(max_length=300)
    email = models.EmailField(max_length=300)
    phone = models.CharField(max_length=25) 
    message = models.TextField()
    created_at          = models.DateTimeField(auto_now_add=True)
    updated_at          = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.id} {self.full_name} {self.email}"

    def __unicode__(self):
        return f"{self.id} {self.full_name} {self.email}"

    class Meta:
        verbose_name = 'Enquiry'
        verbose_name_plural = 'Enquiries'
        ordering = [ "-created_at" ]