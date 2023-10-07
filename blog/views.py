from django.http import HttpResponse
from django.shortcuts import render

from .models import PostModel
# Create your views here.

def post_model_list_view(request):
  qs = PostModel.objects.all()
  print(qs)
  context = {
    'object_list': qs
  }
  return render(request, "blog/list-view.html", context)
