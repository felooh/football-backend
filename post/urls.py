from django.urls import path, include
from .views import *
from .views import PostViewSet
from rest_framework import routers




router = routers.DefaultRouter()
router.register('post', PostViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
