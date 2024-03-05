from django.urls import path, include
from rest_framework_simplejwt.views import TokenRefreshView
from .views import ClientList

app_name = 'client'

urlpatterns = [
    path('create-client/<str:link_name>', ClientList.as_view(), name='create_client'),
]
