from django.test import TestCase
from django.contrib.auth.password_validation import validate_password
import os

class RecipeConfigTest(TestCase):
  def test_secret_key_strength(self):
    SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')
    try:
      validate_password(SECRET_KEY)
    except Exception as e:
      msg = f'Weak secret key {e.messages}'
      self.fail(msg)