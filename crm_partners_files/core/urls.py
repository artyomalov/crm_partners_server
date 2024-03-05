from django.contrib import admin
from django.urls import path, include

api_v1_url = 'api/v1/'

urlpatterns = [
    path('admin/', admin.site.urls),
    path(f'{api_v1_url}user/', include('user.urls'), name='user'),
    path(f'{api_v1_url}link/', include('link.urls'), name='link'),
    path(f'{api_v1_url}client/', include('client.urls'), name='client'),
]
