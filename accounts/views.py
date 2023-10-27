from multiprocessing import context
from django.shortcuts import render
from django.urls import reverse
from django.shortcuts import redirect
from django.contrib.auth import login, get_user_model, logout

from .forms import UserCreationForm, UserLoginForm
from .models import ActivationProfile


User = get_user_model()


def home(request):
  if request.user.is_authenticated:
    context = {
      'user': request.user.username,
      # 'city': request.user.profile.city,
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
    # username = form.cleaned_data.get('username')
    # user_obj = User.objects.get(username__iexact=username)
    user_obj = form.cleaned_data.get('user_obj')
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


def activate_user_view(request, code=None, *args, **kwargs):
  if code:
    act_profile_qs = ActivationProfile.objects.filter(key=code)
    if act_profile_qs.exists() and act_profile_qs.count() == 1:
      act_obj = act_profile_qs.first()
      if not act_obj.expired:
        user_obj = act_obj.user
        user_obj.is_active = True
        user_obj.save()
        act_obj.expired = True
        act_obj.save()
        return redirect('accounts:login')
  # invalid code
  return redirect('accounts:login')