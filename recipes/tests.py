from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.test import TestCase

from .models import Recipe, RecipeIngredient

# Create your tests here.

User = get_user_model()

class UserTestCase(TestCase):
  def setUp(self):
    self.user_a = User.objects.create_user('osama', password='abc123')
  
  def test_user_password(self):
    checked = self.user_a.check_password('abc123')
    self.assertTrue(checked)

class RecipeTestCase(TestCase):
  def setUp(self):
    self.user_a = User.objects.create_user('osama', password='abc123')
    self.recipe_a = Recipe.objects.create(user=self.user_a, name='Grilled chicken')
    self.recipe_b = Recipe.objects.create(user=self.user_a, name='Grilled chicken Tacos')
    self.recipe_count = Recipe.objects.filter(user=self.user_a).count()

    self.recipe_ingredient_a = RecipeIngredient.objects.create(recipe=self.recipe_a, name='Chicken', quantity='1/2', unit='pound')
    self.recipe_ingredient_count = RecipeIngredient.objects.filter(recipe=self.recipe_a).count()

  def test_user_count(self):
    qs = User.objects.all()
    self.assertEqual(qs.count(), 1)

  def test_user_recipe_reverse_count(self):
    user = self.user_a
    qs = user.recipe_set.all()
    self.assertEqual(qs.count(), self.recipe_count)

  def test_user_recipe_forward_count(self):
    qs = Recipe.objects.filter(user=self.user_a)
    self.assertEqual(qs.count(), self.recipe_count)

  def test_recipe_ingredient_reverse_count(self):
    recipe = self.recipe_a
    qs = recipe.recipeingredient_set.all()
    self.assertEqual(qs.count(), self.recipe_ingredient_count)

  def test_recipe_ingredient_count(self):
    qs = RecipeIngredient.objects.filter(recipe=self.recipe_a)
    self.assertEqual(qs.count(), self.recipe_ingredient_count)
  
  def test_user_two_level_relation(self):
    qs = RecipeIngredient.objects.filter(recipe__user=self.user_a)
    self.assertEqual(qs.count(), self.recipe_ingredient_count)

  def test_user_two_level_relation_reverse(self):
    user = self.user_a
    recipeingredient_ids = list(user.recipe_set.all().values_list('recipeingredient__id', flat=True))
    qs = RecipeIngredient.objects.filter(id__in=recipeingredient_ids)
    self.assertEqual(qs.count(), self.recipe_ingredient_count)

  def test_user_two_level_relation_via_recipes(self):
    user = self.user_a
    ids = user.recipe_set.all().values_list("id", flat=True)
    qs = RecipeIngredient.objects.filter(recipe__id__in=ids)
    self.assertEqual(qs.count(), self.recipe_ingredient_count)

  def test_unit_measure_validation(self):
    valid_unit = 'ounce'
    ingredient = RecipeIngredient(
      name = 'New',
      quantity = 10,
      recipe = self.recipe_a,
      unit = valid_unit
    )
    ingredient.full_clean()
    
  def test_unit_measure_validation_error(self):
    invalid_unit = 'wrongunit'
    with self.assertRaises(ValidationError):
      ingredient = RecipeIngredient(
        name = 'New',
        quantity = 10,
        recipe = self.recipe_a,
        unit = invalid_unit
      )
      ingredient.full_clean()

  def test_unit_measure_validation_error_list(self):
    invalid_units = ['wrongunit', 'abc']
    with self.assertRaises(ValidationError):
      for unit in invalid_units:
        ingredient = RecipeIngredient(
          name = 'New',
          quantity = 10,
          recipe = self.recipe_a,
          unit = unit
        )
        ingredient.full_clean()
