from django.urls import path

from tradings import views

urlpatterns = [
    path('', views.send_message, name='send_message')
]
