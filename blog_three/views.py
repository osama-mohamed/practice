from multiprocessing import context
from django.shortcuts import render

from .forms import TestForm, PostModelForm
# Create your views here.


def home(request):
  form = PostModelForm(request.POST or None)
  if form.is_valid():
    form.save()
  context = {
    'form': form
  }
  return render(request, 'forms.html', context)