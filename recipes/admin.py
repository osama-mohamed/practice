from django.contrib import admin
from django.contrib.auth import get_user_model

from .models import Recipe, RecipeIngredient

# Register your models here.

User = get_user_model()

class RecipeInline(admin.StackedInline):
  model = Recipe
  extra = 0

class UserAdmin(admin.ModelAdmin):
  inlines = [RecipeInline]
  list_display = ['username']
admin.site.unregister(User)
admin.site.register(User, UserAdmin)


class RecipeIngredientInline(admin.StackedInline): # TabularInline
  model = RecipeIngredient
  extra = 1
  # fields = ['name', 'quantity', 'unit', 'directions']


class RecipeIngredientAdmin(admin.ModelAdmin):
  list_display = ['recipe', 'name', 'quantity', 'unit', 'active', 'timestamp', 'updated', 'get_recipe_name']
  @admin.display(ordering='recipe__name', description='Recipe Name') # get ForeignKey name
  def get_recipe_name(self, obj):
    return obj.recipe.name
admin.site.register(RecipeIngredient, RecipeIngredientAdmin)


class RecipeAdmin(admin.ModelAdmin):
  inlines = [RecipeIngredientInline]
  list_display = ['name', 'user', 'active']
  readonly_fields = ['timestamp', 'updated']
  raw_id_fields = ['user']
admin.site.register(Recipe, RecipeAdmin)