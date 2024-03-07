from django.db import models


class Link(models.Model):
    link_name = models.CharField(max_length=255, unique=True, verbose_name='Name of the link')
    tg_channel_id = models.CharField(max_length=255, verbose_name='Telegram channel\'s id')
    deal_source = models.CharField(max_length=255, verbose_name='Deal\'s source')
    google_sheets_link = models.CharField(max_length=255, verbose_name='Google sheets link')
    generated_link = models.CharField(max_length=255, verbose_name='Link')
    category = models.CharField(max_length=255, verbose_name='Link\'s category')

    def __str__(self):
        return self.generated_link

    class Meta:
        verbose_name = 'Link'
        verbose_name_plural = 'Links'
