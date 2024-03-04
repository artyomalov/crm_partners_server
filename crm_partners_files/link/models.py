from django.db import models


class Link(models.Model):
    link_name = models.CharField(max_length=255, verbose_name='Name of the link')
    tg_channel_id = models.CharField(max_length=255, verbose_name='Telegram channel\'s id')
    deal_source = models.CharField(max_length=255, verbose_name='Deal\'s source')
    google_sheets_link = models.CharField(max_length=255, verbose_name='Google sheets link')
    generated_link = models.CharField(max_length=255, verbose_name='Link')

    def __str__(self):
        return self.generated_link
