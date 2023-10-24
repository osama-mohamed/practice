from django.shortcuts import render
from django.utils.text import slugify

from .forms import TestForm, PostModelForm


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