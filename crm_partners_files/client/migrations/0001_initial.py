# Generated by Django 5.0.2 on 2024-03-05 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullName', models.CharField(verbose_name='Full name')),
                ('phone_number', models.CharField(verbose_name='Phone_number')),
                ('tg_username', models.CharField(verbose_name='Telegram username')),
                ('comment', models.CharField(verbose_name='Comment')),
            ],
            options={
                'verbose_name': 'Client',
                'verbose_name_plural': 'Clients',
            },
        ),
    ]
