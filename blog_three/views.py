from django.shortcuts import render
from django.utils.text import slugify

from .forms import TestForm, PostModelForm


def home(request):
  form = PostModelForm(request.POST or None)
  if form.is_valid():
    obj = form.save(commit=False)
    obj.slug = slugify(obj.title)
    obj.save()
  context = {
    'form': form
  }
  return render(request, 'forms.html', context)