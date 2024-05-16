
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('grappelli/', include('grappelli.urls')),
    path('admin/', admin.site.urls),

    path('api/v1/auth/', include('djoser.urls')),
    path("api/v1/auth/", include("djoser.urls.jwt")),
]

admin.site.site_title = "Vroomhive Services"
admin.site.site_header = "Vroomhive Inc"
admin.site.index_title = "Vroomhive welcomes you!!!"