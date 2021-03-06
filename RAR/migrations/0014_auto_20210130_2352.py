# Generated by Django 3.1.4 on 2021-01-30 23:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RAR', '0013_car_plate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='km',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='car',
            name='plate',
            field=models.CharField(max_length=8, unique=True),
        ),
        migrations.AlterField(
            model_name='car',
            name='year',
            field=models.IntegerField(),
        ),
    ]
