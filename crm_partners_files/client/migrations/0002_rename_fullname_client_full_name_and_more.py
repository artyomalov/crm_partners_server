# Generated by Django 5.0.2 on 2024-03-05 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='client',
            old_name='fullName',
            new_name='full_name',
        ),
        migrations.AlterField(
            model_name='client',
            name='phone_number',
            field=models.CharField(verbose_name='Phone number'),
        ),
    ]
