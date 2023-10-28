from django.test import TestCase
from django.utils import timezone
from django.utils.text import slugify
import datetime


# Create your tests here.
from blog.models import PostModel as Post

# https://docs.djangoproject.com/en/4.2/topics/testing/overview/

class PostModelTestCase(TestCase):
  def setUp(self):
    Post.objects.create(title='A new title', content='Some content')

  def test_post_model(self):
    obj = Post.objects.get(id=1)
    self.assertEqual(obj.title, 'A new title')
    self.assertEqual(obj.content, 'Some content')
    self.assertTrue(obj.slug is not None)

  def test_post_model_slug(self):
    obj = Post.objects.get(id=1)
    self.assertEqual(obj.slug, 'a-new-title')
    self.assertEqual(obj.slug, slugify(obj.title))
  
  def test_post_model_publish(self):
    obj = Post.objects.get(id=1)
    self.assertEqual(obj.publish, 'draft')
  
  def test_post_model_active(self):
    obj = Post.objects.get(id=1)
    self.assertEqual(obj.active, True)
    self.assertTrue(obj.active is True)
  
  def test_post_model_publish_date(self):
    obj = Post.objects.get(id=1)
    self.assertEqual(obj.publish_date, datetime.date.today())
    self.assertIsNot(obj.publish_date, '')

  def test_post_url(self):
    obj = Post.objects.get(id=1)
    self.assertEqual(obj.get_absolute_url(), '/blog/1/')