# Generated by Django 4.2.6 on 2023-10-20 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products_two', '0003_product_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]
