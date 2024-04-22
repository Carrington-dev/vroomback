from django.contrib import admin
from tradings.models import CarModel, Image, Make, Vehicle


admin.site.register(CarModel)
class ModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'id', 'make')


admin.site.register(Make)
class MakeAdmin(admin.ModelAdmin):
    list_display = ('name', 'id')


admin.site.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ('title', '')


admin.site.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('vehicle', 'image', 'id')

    def photo(self, obj):
        return f"<img { obj.photo.url }height={200} width={150} />"