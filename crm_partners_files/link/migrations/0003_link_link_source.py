# Generated by Django 5.0.2 on 2024-03-05 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('link', '0002_alter_link_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='link',
            name='link_source',
            field=models.CharField(default='partnerToCompany', max_length=255, verbose_name='Source of the link'),
            preserve_default=False,
        ),
    ]
