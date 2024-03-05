from django.db import models


class Client(models.Model):
    full_name = models.CharField(verbose_name='Full name')
    phone_number = models.CharField(verbose_name='Phone number')
    tg_username = models.CharField(verbose_name='Telegram username')
    comment = models.CharField(verbose_name='Comment')

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'
