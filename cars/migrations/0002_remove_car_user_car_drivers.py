# Generated by Django 4.2.6 on 2023-10-28 15:45

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='user',
        ),
        migrations.AddField(
            model_name='car',
            name='drivers',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
