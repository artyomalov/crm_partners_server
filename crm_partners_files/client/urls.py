from django.urls import path, include
from rest_framework_simplejwt.views import TokenRefreshView
from .views import ClientDetail

app_name = 'client'

urlpatterns = [
    path('create-client/<str:link_name>', ClientDetail.as_view(), name='create_client'),
]
