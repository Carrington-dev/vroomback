from django.urls import path, include
from tradings import views

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('countries', viewset=views.CountryViewSet, basename='country')
router.register('cities', viewset=views.CityViewSet, basename='city')
router.register('states', viewset=views.StateViewSet, basename='state')
router.register('makes', viewset=views.MakeViewSet, basename='make')
router.register('vehicles', viewset=views.VehicleViewSet, basename='vehicle')
router.register('models', viewset=views.CarModelViewSet, basename='model')

urlpatterns = [
    path('', views.send_message, name='send_message'),
    path('api/v1/', include(router.urls)),
]
