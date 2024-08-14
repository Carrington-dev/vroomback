from django.contrib import admin

from tradings.utils import MAX_OBJECTS

class ClientAdmin(admin.AdminSite):
    site_header = "Vroomhive Pty Ltd"
    site_title = "Vroomhive ADMIN PORTAL"
    index_title = "Vroomhive welcomes you!!!"

client_admin_site = ClientAdmin(name='client_admin')

# @admin.register(Module, site=client_admin_site)
from django.contrib import admin
from django.utils.safestring import mark_safe
from tradings.actions import duplicate_event, mark_as_democar, mark_as_draft, mark_as_newcar, mark_as_oldcar, mark_as_published, remove_copy_on_title, switch_to_default_thumbnail
from tradings.models import CarModel, City, Color, Country, Enquiry, Image, Make, State, Vehicle, VehicleKeyFeatures, VehicleOtherFeatures

class ImageInline(admin.TabularInline):
    model = Image
    extra = 1

    def has_add_permission(self, request, obj):
        if obj.images.count() >= MAX_OBJECTS:
            return False
        return True



@admin.register(Vehicle, site=client_admin_site)
class VehicleAdmin(admin.ModelAdmin):
    list_display = [ "title", "user", "model", "make", "state", "city", 'year', "price", "mileage", "engine_capacity", "condition", "colour", "top_speed", 
                    "stock", "horse_power",  'status_icon',  "created_at",]
    search_fields = ["title", "model__name", "airbag_quantity", "make__name", "state__name", "city__name", "slug", 'year', "price", "mileage", "engine_capacity", "condition", "colour", "top_speed", ]
    inlines = [
        ImageInline
    ]
    list_per_page = 20

    actions = [
        duplicate_event, mark_as_published, remove_copy_on_title, switch_to_default_thumbnail, mark_as_draft, mark_as_oldcar, mark_as_newcar, mark_as_democar
    ]

    def status_icon(self, obj):
        return obj.status == 'published'

    status_icon.short_description = ('Published')
    status_icon.boolean = True


    def get_queryset(self, request):
        qs = super().get_queryset(request)
        # if request.user.is_superuser:
        #     return qs
        return qs.filter(user=request.user)

@admin.register(Image, site=client_admin_site)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('vehicle', 'photo_url', 'id')
    list_per_page = 20

    def photo_url(self, obj):
        return mark_safe(f"<img src={ obj.photo.url } height={60} width={110} />")

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(vehicle__user=request.user)
    
    def has_add_permission(self, request):
        return False
    
    def has_delete_permission(self, request, obj=None):
        return False
    
@admin.register(VehicleKeyFeatures, site=client_admin_site)
class VehicleOtherFeaturesAdmin(admin.ModelAdmin):
    list_display = [
                    'vehicle', "premium_pheel","sun_roof","premium_audio","navigation",\
                        "front_heated_seats","premium_seat_material","bluetooth",
                        "premium_seat_material","front_heated_seats","remote_engine_start",
                        "blind_spot_System","multi_zone_climate_control","has_roof_rack",
                        "electronic_doors","has_security","push_start_button",    ]
    
    list_per_page = 20

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(vehicle__user=request.user)


@admin.register(VehicleOtherFeatures, site=client_admin_site)
class VehicleOtherFeaturesAdmin(admin.ModelAdmin):
    list_display = [
        'vehicle', 'id'
    ]
    list_per_page = 20

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(vehicle__user=request.user)