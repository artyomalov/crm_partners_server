from django.contrib import admin
from .models import Link


@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    list_display = ['link_name', 'tg_channel_id', 'deal_source', 'generated_link']
    list_display_links = ['link_name', ]
