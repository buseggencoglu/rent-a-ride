# Generated by Django 3.1.4 on 2021-02-03 16:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RAR', '0023_auto_20210203_1619'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='plate',
            field=models.CharField(max_length=10, unique=True),
        ),
        migrations.AlterField(
            model_name='notifications',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 3, 16, 42, 13, 605043)),
        ),
    ]
