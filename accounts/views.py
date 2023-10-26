from multiprocessing import context
from django.shortcuts import render
from django.urls import reverse
from django.shortcuts import redirect

from .forms import UserCreationForm

def home(request):
  if request.user.is_authenticated:
    context = {
      'user': request.user.username,
      'city': request.user.profile.city,
    }
    return render(request, 'accounts/home.html', context)
  
def register(request):
  form = UserCreationForm(request.POST or None)
  if form.is_valid():
    form.save()
    return redirect('accounts:home')
  else:
    form = UserCreationForm()
  context = {
    'form': form,
  }
  return render(request, 'accounts/register.html', context)