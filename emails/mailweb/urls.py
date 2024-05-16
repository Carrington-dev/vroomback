
from django.contrib import admin
from django.urls import path
from mailweb import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/send-welcome-mail', views.HomeView, name='home'),
]
