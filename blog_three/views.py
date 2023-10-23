from multiprocessing import context
from django.shortcuts import render

from .forms import TestForm
# Create your views here.


def home(request):
  form = TestForm(request.POST or None)
  if form.is_valid():
    print(form.cleaned_data.get('some_text'))
  # if request.method == 'POST':
  #   print(request.POST.get('some_text'))
  context = {
    'form': form
  }
  return render(request, 'forms.html', context)