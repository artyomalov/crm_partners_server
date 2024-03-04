# Generated by Django 5.0.2 on 2024-03-04 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, verbose_name='ID')),
                ('link_name', models.CharField(max_length=255, verbose_name='Name of the link')),
                ('tg_channel_id', models.CharField(max_length=255, verbose_name="Telegram channel's id")),
                ('deal_source', models.CharField(max_length=255, verbose_name="Deal's source")),
                ('google_sheets_link', models.CharField(max_length=255, verbose_name='Google sheets link')),
                ('generated_link', models.CharField(max_length=255, verbose_name='Link')),
            ],
        ),
    ]
