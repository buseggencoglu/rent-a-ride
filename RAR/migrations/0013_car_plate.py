# Generated by Django 3.1.4 on 2021-01-30 23:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RAR', '0012_remove_car_plate'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='plate',
            field=models.CharField(default='', max_length=8, unique=True),
        ),
    ]
