from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages

from .forms import PostModelForm
from .models import PostModel


@login_required
def post_model_update_view(request, id=None):
  obj = get_object_or_404(PostModel, id=id)
  form = PostModelForm(request.POST or None, instance=obj)
  context = {
    'form': form,
    # 'object': obj,
  }
  if form.is_valid():
    obj = form.save(commit=False)
    obj.save()
    messages.success(request, 'Updated successfully!')
    return redirect('blog:detail', id=obj.id)
  return render(request, 'blog/update-view.html', context)


def post_model_delete_view(request, id=None):
  obj = get_object_or_404(PostModel, id=id)
  if request.method == 'POST':
    obj.delete()
    messages.success(request, 'Deleted successfully!')
    return redirect('blog:list')
  context = {
    'object': obj
  }
  return render(request, 'blog/delete-view.html', context)


@login_required
def post_model_create_view(request):
  # if request.method == 'POST':
  #   # print(request.POST)
  #   form = PostModelForm(request.POST)
  #   if form.is_valid():
  #     form.save(commit=False)
  #     print(form.cleaned_data)

  form = PostModelForm(request.POST or None)
  context = {
    'form': form
  }
  if form.is_valid():
    obj = form.save(commit=False)
    obj.save()
    messages.success(request, 'Created successfully!')
    # context = {
    #   'form': PostModelForm()
    # }
    # return HttpResponseRedirect(f'/blog/{obj.id}')
    return redirect('blog:detail', id=obj.id)
  return render(request, 'blog/create-view.html', context)


def post_model_detail_view(request, id):
  obj = get_object_or_404(PostModel, id=id)

  # qs = PostModel.objects.filter(id=1)
  # obj = None
  # if not qs.exists() and qs.count() != 1:
  #   raise Http404
  # else:
  #   obj = qs.first()

  # try:
  #   obj = PostModel.objects.get(id=1)
  # except:
  #   raise Http404

  # obj = PostModel.objects.get(id=1)
  context = {
    'object': obj
  }
  return render(request, 'blog/detail-view.html', context)


def post_model_list_view(request):
  qs = PostModel.objects.all()
  context = {
    'object_list': qs
  }
  return render(request, 'blog/list-view.html', context)


# @login_required(login_url='/login')
def login_required_view(request, id):
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


