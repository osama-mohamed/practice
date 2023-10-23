from multiprocessing import context
from django.shortcuts import render

from .forms import SearchForm
# Create your views here.


def home(request):
  form = SearchForm()
  context = {
    'form': form
  }
  return render(request, 'forms.html', context)