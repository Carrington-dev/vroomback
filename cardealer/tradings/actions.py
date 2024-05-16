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

mark_as_draft.short_description = "Save selected vehicles as draft"



def mark_as_published(self, request, queryset):
    queryset.update(status="published")


mark_as_published.short_description = "Mark selected vehicles as published"