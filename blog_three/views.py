from multiprocessing import context
from django.shortcuts import render

from .forms import TestForm
# Create your views here.


def home(request):
  form = TestForm()
  if request.method == 'POST':
    print(request.POST.get('some_text'))
  context = {
    'form': form
  }
  return render(request, 'forms.html', context)