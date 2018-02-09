# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-01-26 09:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20180126_1108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='avg_rate',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='number_of_sales',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='number_of_views',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
