# Generated by Django 4.2.6 on 2023-10-24 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_three', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='publish',
            field=models.DateField(default='2023-10-24'),
        ),
    ]
