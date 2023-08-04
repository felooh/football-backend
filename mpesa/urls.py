from django.urls import path
from . import views

urlpatterns = [
    path('accesstoken/', views.get_access_token, name='get_access_token'),
    path('initiate/', views.initiate_stk_push, name='initiate_stk_push'),
    path('query/', views.query_stk_status, name='query_stk_status'),
]
