# Generated by Django 3.1.4 on 2021-02-02 20:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RAR', '0021_auto_20210202_2011'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='age',
        ),
        migrations.AddField(
            model_name='customer',
            name='birthDate',
            field=models.DateField(default=datetime.datetime(2021, 2, 2, 20, 45, 42, 406927)),
        ),
        migrations.AlterField(
            model_name='notifications',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 2, 20, 45, 42, 409918)),
        ),
    ]
