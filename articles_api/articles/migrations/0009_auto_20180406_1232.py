# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-04-06 10:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0008_auto_20180405_2220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='img',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
