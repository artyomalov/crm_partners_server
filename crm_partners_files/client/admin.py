from django.contrib import admin
from .models import Client


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'phone_number', 'tg_username', ]
    list_display_links = ['full_name', ]
