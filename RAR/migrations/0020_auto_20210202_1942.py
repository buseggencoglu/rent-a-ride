# Generated by Django 3.1.4 on 2021-02-02 19:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RAR', '0019_auto_20210201_2251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notifications',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 2, 19, 42, 34, 870583)),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='customer_name',
            field=models.CharField(blank=True, default='', max_length=36, null=True),
        ),
    ]