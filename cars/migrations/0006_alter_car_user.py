# Generated by Django 4.2.6 on 2023-10-28 16:47

import cars.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cars', '0005_remove_car_passengers_car_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='user',
            field=models.ForeignKey(on_delete=models.SET(cars.models.set_delete_user), to=settings.AUTH_USER_MODEL),
        ),
    ]
