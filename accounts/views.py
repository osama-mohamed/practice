from multiprocessing import context
from django.shortcuts import render
from django.urls import reverse
from django.shortcuts import redirect
from django.contrib.auth import login, get_user_model, logout

from .forms import UserCreationForm, UserLoginForm


User = get_user_model()


def home(request):
  if request.user.is_authenticated:
    context = {
      'user': request.user.username,
      'city': request.user.profile.city,
    }
    return render(request, 'accounts/home.html', context)
  context = {
    'user': request.user,
    }
  return render(request, 'accounts/home.html', context)
  
def register(request):
  form = UserCreationForm(request.POST or None)
  if form.is_valid():
    form.save()
    return redirect('accounts:login')
  else:
    form = UserCreationForm()
  context = {
    'form': form,
    'btn': 'Register',
  }
  return render(request, 'accounts/register.html', context)


def user_login(request):
  form = UserLoginForm(request.POST or None)
  if form.is_valid():
    username = form.cleaned_data.get('username')
    user_obj = User.objects.get(username__iexact=username)
    login(request, user_obj)
    return redirect('accounts:home')
  context = {
    'form': form,
    'btn': 'Login',
  }
  return render(request, 'accounts/login.html', context)


def user_logout(request):
  logout(request)
  return redirect('accounts:login')