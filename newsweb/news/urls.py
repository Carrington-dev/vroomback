from django.urls import path, include
from rest_framework.routers import DefaultRouter
from news.views import CategoryViewSet, PostViewSet, TagViewSet

router =  DefaultRouter()
router.register("posts", PostViewSet, basename="post")
router.register("categories", CategoryViewSet, basename="categories")
router.register("tags", TagViewSet, basename="tag")

urlpatterns = [
    path('', include(router.urls))
]
