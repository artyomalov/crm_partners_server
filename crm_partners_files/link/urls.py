from django.urls import path, include
from rest_framework_simplejwt.views import TokenRefreshView
from .views import LinkDetail, LinkList, LinkSearch

app_name = 'link'

urlpatterns = [
    path('create-link/', LinkDetail.as_view(), name='create_link'),
    path('delete-link/', LinkDetail.as_view(), name='delete_link'),
    path('get-all-links', LinkList.as_view(), name='get_links'),
    path('delete-selected-links', LinkList.as_view(), name='delete_selected_links'),
    path('search-links', LinkSearch.as_view(), name='search_links')
]
