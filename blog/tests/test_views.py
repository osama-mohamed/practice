from django.test import TestCase
from django.urls import reverse


from blog.models import PostModel as Post


class PostViewsTestCase(TestCase):
  def setUp(self):
    Post.objects.create(title='A new title', content='Some content')

  def test_list_view(self):
    list_url = reverse('blog:list')
    response = self.client.get(list_url)
    self.assertEqual(response.status_code, 200)
  
  def test_detail_view(self):
    obj = Post.objects.get(id=1)
    response = self.client.get(obj.get_absolute_url())
    self.assertEqual(response.status_code, 200)
  
  def test_update_view(self):
    obj = Post.objects.get(id=1)
    update_url = reverse('blog:update', kwargs={'id': obj.id})
    response = self.client.get(update_url)
    self.assertEqual(response.status_code, 302)
  
  def test_delete_view(self):
    obj = Post.objects.get(id=1)
    delete_url = reverse('blog:delete', kwargs={'id': obj.id})
    response = self.client.get(delete_url)
    self.assertEqual(response.status_code, 200)