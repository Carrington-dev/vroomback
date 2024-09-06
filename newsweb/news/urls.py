from django.urls import path, include
from rest_framework.routers import DefaultRouter
from news.views import CategoryViewSet, PostViewSet

router =  DefaultRouter()
router.register("posts", PostViewSet, basename="post")
router.register("categories", CategoryViewSet, basename="categories")

urlpatterns = [
    path('', include(router.urls))
]
