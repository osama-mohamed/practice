from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render

from .models import PostModel


def post_model_list_view(request):
  qs = PostModel.objects.all()
  context = {
    'object_list': qs
  }
  return render(request, 'blog/list-view.html', context)


# @login_required(login_url='/login')
def login_required_view(request):
  qs = PostModel.objects.all()
  print(request.user)
  if request.user.is_authenticated:
    print(f'#{request.user.id} is : {request.user.username}')
    template = 'blog/list-view.html'
  else:
    print("Nope, not logged in")
    template = 'blog/list-view-public.html'
    return HttpResponseRedirect('/login')
    # raise Http404
  context = {
    'object_list': qs
  }
  return render(request, template, context)


