# Generated by Django 3.2.9 on 2021-12-07 08:00

from django.db import migrations, models
import django.db.models.deletion
import recipes.models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0003_recipeingredient_quantity_as_float'),
    ]

    operations = [
        migrations.CreateModel(
            name='RecipeIngredientImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=recipes.models.recipe_ingredient_image_upload_handler)),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipes.recipe')),
            ],
        ),
    ]
