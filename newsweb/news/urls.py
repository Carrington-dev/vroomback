from django.urls import path, include
from rest_framework.routers import DefaultRouter
from news.views import CategoryViewSet, ContactViewSet, PostViewSet, TagViewSet

router =  DefaultRouter()
router.register("posts", PostViewSet, basename="post")
router.register("categories", CategoryViewSet, basename="categories")
router.register("tags", TagViewSet, basename="tag")
router.register("contacts", ContactViewSet, basename="contact")

urlpatterns = [
    path('', include(router.urls))
]
