# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-01-03 12:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='url',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='url',
            name='shortcode',
            field=models.CharField(blank=True, max_length=15, unique=True),
        ),
    ]
