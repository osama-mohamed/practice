from django.test import TestCase

from blog.models import PostModel as Post
from blog.forms import PostModelForm


# class PostFormTest(TestCase):

#   def test_valid_form(self):
#     obj = Post.objects.create(title='A new form title', content='Some form content', slug='a-new-form-title')
#     print(obj.active, obj.id, obj.publish, obj.content, obj.title, obj.slug)
#     # data = {'title': obj.title, 'content': obj.content, 'slug': obj.slug, 'publish': obj.publish, 'active': obj.active}
#     data = {'title': obj.title}
#     form = PostModelForm(data=data)
#     self.assertTrue(form.is_valid())
#     self.assertEqual(form.cleaned_data.get('title'), obj.title)
#     self.assertEqual(form.cleaned_data.get('content'), obj.content)

  
