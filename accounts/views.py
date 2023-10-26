from django.shortcuts import render


def home(request):
  if request.user.is_authenticated:
    context = {
      'user': request.user.username,
      'city': request.user.profile.city,
    }
    return render(request, 'accounts/home.html', context)