from django.contrib import admin
from django.urls import include, path
from vroomweb import settings
from django.conf.urls.static import static

version = 'version'

urlpatterns = [
    path('grappelli/', include('grappelli.urls')),
    path('admin/', admin.site.urls),
    path(f"api/{version}/", include("security.urls")),
    path(f"api/{version}/", include("news.urls")),
    path(f'api/{version}/auth/', include('djoser.urls')),
    path(f"api/{version}/auth/", include("djoser.urls.jwt")),

]


admin.site.site_title = "Vroohmive Inc"
admin.site.site_header = "Vroohmive Pty Ltd"
admin.site.index_title = "Vroohmive welcomes you!!!"


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)