# Generated by Django 3.1.4 on 2021-02-02 21:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RAR', '0021_auto_20210202_2011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notifications',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 2, 21, 0, 13, 704236)),
        ),
    ]
