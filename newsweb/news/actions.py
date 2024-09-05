from django.shortcuts import get_object_or_404
from django.contrib import messages

from news.models import Post

def duplicate_post(modeladmin, request, queryset):
        for object in queryset:
            try:
                obj = get_object_or_404(Post, pk=object.id)
                obj.title = str(object.title) + f" Copy"
                obj.pk = None
                obj.save()
                messages.success(request, f"{object.title} has been dublicated.")
            except:
                pass

duplicate_post.short_description = "Duplicate selected posts"

def mark_as_draft(self, request, queryset):
    queryset.update(status="draft")
    messages.success(request, f"Saved selected posts as draft")

mark_as_draft.short_description = "Save selected posts as draft"