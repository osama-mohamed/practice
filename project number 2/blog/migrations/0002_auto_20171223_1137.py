# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-23 09:37
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 23, 11, 37, 52, 868366)),
        ),
    ]
