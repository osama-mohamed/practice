from django.shortcuts import render
from django.utils.text import slugify
from django.forms import formset_factory, modelformset_factory


from .forms import TestForm, PostModelForm
from .models import Post


def home(request):
  form = PostModelForm(request.POST or None)
  if form.is_valid():
    obj = form.save(commit=False)
    obj.slug = slugify(obj.title)
    obj.save()
  if form.has_error:
    print(form.errors.as_json(), form.errors.as_text(), form.errors.as_data())
    data = form.errors.items()
    for key, value in data:
      error_str = f'{key}: {value.as_text()}'
      print(error_str)
  context = {
    'form': form
  }
  return render(request, 'forms.html', context)



# def formset_view(request):
#   TestFormset = formset_factory(TestForm, extra=2)
#   formset = TestFormset()
#   if formset.is_valid():
#     for form in formset:
#       print(form.cleaned_data)
#   context = {
#     'formset': formset
#   }
#   return render(request, 'blog_three/formset_view.html', context)


def formset_view(request):
  PostModelFormset = modelformset_factory(Post, fields=['user', 'title', 'image'], extra=2)
  formset = PostModelFormset()
  if formset.is_valid():
    formset.save()
    # for form in formset:
    #   print(form.cleaned_data)
  context = {
    'formset': formset
  }
  return render(request, 'blog_three/formset_view.html', context)