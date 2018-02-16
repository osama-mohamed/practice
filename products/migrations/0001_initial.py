# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-02-16 07:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('price', models.PositiveIntegerField()),
                ('quantity', models.PositiveIntegerField()),
                ('discount', models.FloatField(blank=True, default=0, null=True)),
                ('number_of_sales', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('number_of_views', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('avg_rate', models.FloatField(blank=True, default=0, null=True)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='')),
                ('added', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
