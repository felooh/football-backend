from django.urls import path, include
from .views import *
from rest_framework import routers
from .views import UsersViewSet




router = routers.DefaultRouter()
router.register('user', UsersViewSet)
# router.register()
urlpatterns=[
    
        path('', include(router.urls)),
        path('logout/', LogoutView.as_view()),
        path('api/get-user/', GetLoggedInUser.as_view(), name="getUser"),
        path('api/update-user/', UpdateUser.as_view(), name="update-user")

        
]
