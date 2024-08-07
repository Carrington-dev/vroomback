from django.contrib import admin
from tradings.actions import duplicate_event, mark_as_democar, mark_as_draft, mark_as_newcar, mark_as_oldcar, mark_as_published
from tradings.models import CarModel, City, Color, Country, Enquiry, Image, Make, State, Vehicle, VehicleKeyFeatures, VehicleOtherFeatures

class ImageInline(admin.TabularInline):
    model = Image
    extra = 1

@admin.register(CarModel)
class ModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'id', 'make')


@admin.register(Make)
class MakeAdmin(admin.ModelAdmin):
    list_display = ('name', 'id')


@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = [ 'slug', "title", "model", "make", "state", "city", 'year', "price", "mileage", "engine_capacity", "condition", "colour", "top_speed", 
                    "stock", "horse_power", "airbag_quantity", 'status_icon',  "created_at",]
    search_fields = ["title", "model__name", "make__name", "state__name", "city__name", "slug", 'year', "price", "mileage", "engine_capacity", "condition", "colour", "top_speed", ]
    inlines = [
        ImageInline
    ]
    list_per_page = 20

    actions = [
        duplicate_event, mark_as_published, mark_as_draft, mark_as_oldcar, mark_as_newcar, mark_as_democar
    ]

    def status_icon(self, obj):
        return obj.status == 'published'

    status_icon.short_description = ('Published')
    status_icon.boolean = True

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('vehicle', 'photo', 'id')
    list_per_page = 20
    def photo(self, obj):
        return f"<img { obj.photo.url } height={200} width={150} />"

@admin.register(State)
class StateAdmin(admin.ModelAdmin):
    list_display = ('name', 'country', 'id', )

@admin.register(Enquiry)
class EnquiryAdmin(admin.ModelAdmin):
    list_display = [ "id", "vehicle", "full_name", "email", "phone", "message", ]
    list_per_page = 20

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('name', 'country' ,  'id', )
    list_per_page = 20

@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    list_display = ('name', 'id', 'hexadecimal',)
    list_per_page = 20

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('name', 'id', 'created_at', 'updated_at', )
    list_per_page = 20

@admin.register(VehicleKeyFeatures)
class VehicleOtherFeaturesAdmin(admin.ModelAdmin):
    list_display = [
                    'vehicle', "premium_pheel","sun_roof","premium_audio","navigation",\
                        "front_heated_seats","premium_seat_material","bluetooth",
                        "premium_seat_material","front_heated_seats","remote_engine_start",
                        "blind_spot_System","multi_zone_climate_control","has_roof_rack",
                        "electronic_doors","has_security","push_start_button",    ]
    
    list_per_page = 20


@admin.register(VehicleOtherFeatures)
class VehicleOtherFeaturesAdmin(admin.ModelAdmin):
    list_display = [
        'vehicle', 'id'
    ]
    list_per_page = 20
