from django.test import TestCase
from django.utils.text import slugify


from .models import Product


class ProductTestCase(TestCase):
  # fixtures = ['products/fixtures/products/products.json']

  def create_draft_items(self):
    data = {
      'a': {
        'title': 'Draft item 1', 'price': 99.99,
      },
      'b': {
        'title': 'Draft item 2', 'price': 99.99,
      },
      'c': {
        'title': 'Draft item 3', 'price': 99.99,
      },
    }
    self.draft_a = Product.objects.create(**data.get('a'))
    self.draft_b = Product.objects.create(**data.get('b'))
    self.draft_c = Product.objects.create(**data.get('c'))
    self.draft_count = 3
  
  def create_published_items(self):
    data = {
      'a': {
        'title': 'Draft item 1', 
        'price': 99.99, 
        'state': Product.ProductStateOptions.PUBLISH,
      },
      'b': {
        'title': 'Draft item 2', 
        'price': 99.99, 
        'state': Product.ProductStateOptions.PUBLISH,
      },
      'c': {
        'title': 'Draft item 3', 
        'price': 99.99, 
        'state': Product.ProductStateOptions.PUBLISH,
      },
    }
    self.pub_a = Product.objects.create(**data.get('a'))
    self.pub_b = Product.objects.create(**data.get('b'))
    self.pub_c = Product.objects.create(**data.get('c'))
    self.pub_count = 3
  
  def create_unique_slug_items(self):
    non_unique_title = 'This is a title for slugify only it should not work anywere else'
    data = {
      'a': {
        'title': non_unique_title, 
        'price': 99.99, 
      },
      'b': {
        'title': non_unique_title, 
        'price': 99.99, 
      },
      'c': {
        'title': non_unique_title, 
        'price': 99.99, 
      },
    }
    self.slug_title = non_unique_title
    self.slug_slug = slugify(non_unique_title)
    self.slug_a = Product.objects.create(**data.get('a'))
    self.slug_b = Product.objects.create(**data.get('b'))
    self.slug_c = Product.objects.create(**data.get('c'))
    self.unique_slugs_count = 3

  def setUp(self):
    self.create_draft_items()
    self.create_published_items()
    self.create_unique_slug_items()

  def test_draft_items(self):
    qs = Product.objects.filter(state=Product.ProductStateOptions.DRAFT)
    self.assertTrue(qs.exists())
  
  def test_draft_count(self):
    qs = Product.objects.filter(state=Product.ProductStateOptions.DRAFT)
    self.assertEqual(qs.count(), self.draft_count + self.unique_slugs_count)
  
  def test_pub_count(self):
    qs = Product.objects.filter(state=Product.ProductStateOptions.PUBLISH)
    self.assertEqual(qs.count(), self.pub_count)
  
  def test_pub_count_manager(self):
    qs = Product.objects.published()
    self.assertEqual(qs.count(), self.pub_count)
  
  def test_pub_count_queryset_filter(self):
    qs_manager = Product.objects.published()
    qs = Product.objects.all().published()
    self.assertEqual(qs.count(), self.pub_count)
    self.assertEqual(qs.count(), qs_manager.count(), self.pub_count)
    qs_manager_ids = list(qs_manager.values_list('id', flat=True))
    qs_ids = list(qs.values_list('id', flat=True))
    self.assertEqual(qs_ids, qs_manager_ids)
    self.assertEqual(len(qs_ids), len(qs_manager_ids), self.pub_count)

  
  def test_pub_property(self):
    self.assertTrue(self.pub_a.is_published)
    self.assertTrue(self.pub_b.is_published)
    self.assertTrue(self.pub_c.is_published)
  
  def test_queryset_exists(self):
    qs = Product.objects.all()
    self.assertTrue(qs.exists())

  def test_slug_count(self):
    qs = Product.objects.filter(slug__icontains=self.slug_slug)
    self.assertEqual(qs.count(), self.unique_slugs_count)

  def test_slug_title_signal(self):
    self.assertEqual(self.slug_a.slug, self.slug_slug)
  
  def test_slug_unique(self):
    self.assertEqual(self.slug_slug, self.slug_a.slug)
    self.assertNotEqual(self.slug_slug, self.slug_b.slug)
    self.assertNotEqual(self.slug_slug, self.slug_c.slug)
    self.assertNotEqual(self.slug_b.slug, self.slug_c.slug)
    self.assertNotEqual(self.slug_a.slug, self.slug_b.slug, self.slug_c.slug)
  
