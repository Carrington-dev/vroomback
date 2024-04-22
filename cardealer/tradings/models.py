import uuid
from django.db import models
from django_resized import ResizedImageField

from tradings.utils import CONDITION, FUEL_TYPES

class Make(models.Model):
    id = models.UUIDField( 
         primary_key = True, 
         default = uuid.uuid4, 
         editable = False)
    name = models.CharField(max_length=254, unique=True)

    def __str__(self):
        return f"{self.name}" 

    def __unicode__(self):
        return f"{self.name}"
    
class CarModel(models.Model):
    id = models.UUIDField( 
         primary_key = True, 
         default = uuid.uuid4, 
         editable = False)
    name = models.CharField(max_length=254, unique=True)
    make = models.ForeignKey(Make, related_name="models", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}" 

    def __unicode__(self):
        return f"{self.name}"


class Vehicle(models.Model):
    id = models.UUIDField( 
         primary_key = True, 
         default = uuid.uuid4, 
         editable = False)
    title = models.CharField(max_length=254)
    make = models.ForeignKey(Make, related_name="make_vehicles", on_delete=models.CASCADE)
    model = models.ForeignKey(CarModel, related_name="vehicles", on_delete=models.CASCADE)
    engine_capacity = models.IntegerField(default=0)
    mileage = models.IntegerField(default=0)
    fuel = models.CharField(max_length=100, choices=FUEL_TYPES, default='Petrol')
    condition = models.CharField(max_length=100, choices=CONDITION, default='New Car')
    colour = models.CharField(max_length=100, default='White')
    engine_size = models.CharField(max_length=100, default='White')

    def __str__(self):
        return f"{self.title}"

    def __unicode__(self):
        return f"{self.title}"
    

class VehicleFeatures(models.Model):
    id = models.UUIDField( 
         primary_key = True, 
         default = uuid.uuid4, 
         editable = False)
    vehicle = models.OneToOneField(Vehicle, on_delete=models.CASCADE)
    
    
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
    photo = ResizedImageField(size=[1080, 1440], crop=['middle', 'center'], upload_to='car/photos/%Y/%m/%d/')


    def __str__(self):
        return f"{self.vehicle.title}"

    def __unicode__(self):
        return f"{self.vehicle.title}"