from django.urls import path, include
from rest_framework_simplejwt.views import TokenRefreshView
from .views import LinkDetail

app_name = 'link'

urlpatterns = [
    path('create-link/', LinkDetail.as_view(), name='create_link'),
    path('delete-link/', LinkDetail.as_view(), name='delete-link'),
]
