from django.shortcuts import get_object_or_404
from django.contrib import messages

from tradings.models import Vehicle

def duplicate_event(modeladmin, request, queryset):
        for object in queryset:
            try:
                #obj = Vehicle.objects.get(pk=object.id)
                obj = get_object_or_404(Vehicle, pk=object.id)
                obj.title = str(object.title) + f" Copy"
                obj.pk = None
                obj.slug = 'replace'
                obj.save()
                messages.success(request, f"{object.title} has been dublicated.")
            except:
                pass

duplicate_event.short_description = "Duplicate selected vehicles"


def mark_as_draft(self, request, queryset):
    queryset.update(status="draft")
    messages.success(request, f"Saved selected vehicles as draft")

mark_as_draft.short_description = "Save selected vehicles as draft"

def mark_as_oldcar(self, request, queryset):
    queryset.update(condition="used")
    messages.success(request, f"Saved selected vehicles as used")

mark_as_oldcar.short_description = "Save selected vehicles as used"

def mark_as_newcar(self, request, queryset):
    queryset.update(condition="new")
    messages.success(request, f"Saved selected vehicles as new")

mark_as_newcar.short_description = "Save selected vehicles as new"

def mark_as_democar(self, request, queryset):
    queryset.update(condition="demo")
    messages.success(request, f"Saved selected vehicles as demo")

mark_as_democar.short_description = "Save selected vehicles as demo"



def mark_as_published(self, request, queryset):
    queryset.update(status="published")
    messages.success(request, f"Marked selected vehicles as published")

mark_as_published.short_description = "Mark selected vehicles as published"

def switch_to_default_thumbnail(self, request, queryset):
    queryset.update(photo="vehicle/car.jpg")
    messages.success(request, f"Switch selected vehicles photos to defaults")

switch_to_default_thumbnail.short_description = "Switch selected vehicles photos to defaults"


def remove_copy_on_title(modeladmin, request, queryset):
        for object in queryset:
            try:
                #obj = Vehicle.objects.get(pk=object.id)
                obj = get_object_or_404(Vehicle, pk=object.id)
                obj.title = str(object.title.replace("Copy", "")).strip()
                obj.save()
                messages.success(request, f"{object.title} has been updated.")
            except:
                pass

remove_copy_on_title.short_description = "Copy removed on selected vehicles"
