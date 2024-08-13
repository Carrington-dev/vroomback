from django.contrib import admin
from django.urls import include, path
from django.urls import path, include
from vroomweb.settings import settings
from django.conf.urls.static import static

urlpatterns = [
    path('grappelli/', include('grappelli.urls')),
    path('admin/', admin.site.urls),
    path("", include("tradings.urls")),
    path("api/v1/", include("security.urls")),

]


admin.site.site_title = "Vroohmive Inc"
admin.site.site_header = "Vroohmive Pty Ltd"
admin.site.index_title = "Vroohmive welcomes you!!!"


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)