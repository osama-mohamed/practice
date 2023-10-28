from django.test import TestCase, RequestFactory
from django.urls import reverse
from django.contrib.auth.models import AnonymousUser
from django.contrib.auth import get_user_model


from blog.models import PostModel as Post
from blog.views import post_model_update_view, post_model_create_view


User = get_user_model()


class PostViewsAuthTestCase(TestCase):
  def setUp(self):
    self. factory = RequestFactory()
    self.user = User.objects.create(
      username='testuser',
      password='testpass123'
    )
    Post.objects.create(title='A new title', content='Some content')

  def test_user_auth(self):
    obj = Post.objects.get(id=1)
    update_url = reverse('blog:update', kwargs={'id': obj.id})
    request = self.factory.get(update_url)
    request.user = self.user
    response = post_model_update_view(request, id=obj.id)
    self.assertEqual(response.status_code, 200)
  
  def test_user_create(self):
    obj = Post.objects.create(title='New Post Tilte')
    create_url = reverse('blog:create')
    request = self.factory.post(create_url)
    request.user = self.user
    response = post_model_create_view(request)
    self.assertEqual(response.status_code, 200)

  
  def test_update_view(self):
    obj = Post.objects.get(id=1)
    update_url = reverse('blog:update', kwargs={'id': obj.id})
    response = self.client.get(update_url)
    self.assertEqual(response.status_code, 302)

  
  def test_empty_page(self):
    page = '/dfedfeafea/fcewfwea/'
    request = self.factory.get(page)
    request.user = self.user
    response = post_model_create_view(request)
    self.assertEqual(response.status_code, 200)
  
  def test_unauth_user(self):
    obj = Post.objects.get(id=1)
    update_url = reverse('blog:update', kwargs={'id': obj.id})
    request = self.client.get(update_url)
    request.user = AnonymousUser()
    self.assertEqual(request.status_code, 302)