# Generated by Django 3.1.4 on 2021-02-03 16:19

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RAR', '0022_auto_20210202_2100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='plate',
            field=models.CharField(max_length=10, unique=True, validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(10)]),
        ),
        migrations.AlterField(
            model_name='notifications',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 3, 16, 19, 57, 935413)),
        ),
    ]
