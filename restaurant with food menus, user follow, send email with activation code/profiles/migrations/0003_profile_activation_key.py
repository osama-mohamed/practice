# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-01-19 16:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_auto_20180119_1339'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='activation_key',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]
