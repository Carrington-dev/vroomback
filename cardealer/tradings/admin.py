from functools import cache
from django.contrib import admin
from django.utils.safestring import mark_safe
from tradings.utils import MAX_OBJECTS
from tradings.actions import duplicate_event, mark_as_accidentcar, mark_as_democar, mark_as_draft, mark_as_newcar, mark_as_oldcar, mark_as_published, remove_copy_on_title, switch_to_default_thumbnail
from tradings.models import CarModel, City, Color, Country, Enquiry, Image, Make, State, Variant, Vehicle, VehicleKeyFeatures, VehicleOtherFeatures


class VariantInline(admin.TabularInline):
    model = Variant
    fields = ['model', 'name',]
    extra = 0

class ImageInline(admin.TabularInline):
    model = Image
    extra = 1

    def has_add_permission(self, request, obj):
        if obj is not None and obj.images.count() >= MAX_OBJECTS:
            return False
        return True

@admin.register(CarModel)
class ModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'id', 'make', 'variants',)

    inlines = [
        VariantInline
    ]

    # @cache
    def variants(self, obj):
        return ", ".join([ variant.name for variant in obj.variants.all()])


@admin.register(Make)
class MakeAdmin(admin.ModelAdmin):
    list_display = ('name', 'id')

    

@admin.register(Variant)
class VariantAdmin(admin.ModelAdmin):
    list_display = ('name', 'id')

    

@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = [ "title", "user", "type", "model", "make", "state", "city", 'year', "price", "mileage", "condition", "colour", "top_speed", 
                       'status_icon',  "created_at", 'photo_url']
    search_fields = ["title", 'type', "model__name", "airbag_quantity", "make__name", "state__name", "city__name", "slug", 'year', "price", "mileage", "engine_capacity", "condition", "colour", "top_speed", ]
    actions = [ duplicate_event, mark_as_published, mark_as_accidentcar, remove_copy_on_title, switch_to_default_thumbnail, mark_as_draft, mark_as_oldcar, mark_as_newcar, mark_as_democar ]
    list_filter   = [ "user", "model__name", "make__name", "state__name", "city__name", "year"]
    inlines = [
        ImageInline
    ]
    list_display_links = ['title']
    list_editable = [  "type", "user", "model", "make", "state", "city", 'year', "price", "mileage", "condition", "colour", "top_speed", 
                      ]
    list_per_page = 40

    def photo_url(self, obj):
        print("main", obj.photo.url)
        return mark_safe(f'<img src="{ obj.photo.url }" height={60} width={110} />')
    


    def status_icon(self, obj):
        return obj.status == 'published'

    status_icon.short_description = ('Published')
    status_icon.boolean = True

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('vehicle', 'photo_url', 'id')
    list_per_page = 20

    def photo_url(self, obj):
        print("images", obj.photo.url)
        return mark_safe(f"<img src={ obj.photo.url } height={60} width={110} />")
    
    def has_add_permission(self, request):
        return False
    
    def has_delete_permission(self, request, obj=None):
        return False

    

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
