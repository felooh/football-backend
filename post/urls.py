from django.urls import path, include
from .views import *
from .views import PostViewSet
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static



app_name="post"
router = routers.DefaultRouter()
router.register('', PostViewSet, basename="PostViewSet")

urlpatterns = [
    path('', include(router.urls)),
] 

