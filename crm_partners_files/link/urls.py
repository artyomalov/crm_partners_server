from django.urls import path, include
from rest_framework_simplejwt.views import TokenRefreshView
from .views import LinkDetail, LinkList

app_name = 'link'

urlpatterns = [
    path('create-link/', LinkDetail.as_view(), name='create_link'),
    path('delete-link/', LinkDetail.as_view(), name='delete-link'),
    path('get-all-links', LinkList.as_view(), name='create_client'),
    path('delete-selected-links', LinkList.as_view(), name='create_client'),
]
