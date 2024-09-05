from django.urls import include
from rest_framework.routers import DefaultRouter
from news.views import PostViewSet

router =  DefaultRouter()
router.register("posts", PostViewSet, basename="post")

urlpatterns = [
    path()
]
