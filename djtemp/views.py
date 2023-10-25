import datetime
from django.contrib import messages
from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.shortcuts import redirect

from .forms import PostModelForm
from .models import PostModel


def some_test_view(request):
  some_list = ['abc', 123, 'item4', 'another']
  context = {
    'viewTitle': 'This is awesome Capt',
    'abc': 300,
    'addNum': 300,
    'today': datetime.datetime.now().today(),
    'object_list': some_list,
  }
  return render(request, 'djtemp/test-view.html', context)


def post_model_list_view(request):
  query = request.GET.get('q', None)
  qs = PostModel.objects.all()
  if query is not None:
    qs = qs.filter(
      Q(title__icontains=query) |
      Q(content__icontains=query) |
      Q(slug__icontains=query)
    )
  context = {
    'object_list': qs,
  }
  return render(request, 'djtemp/list-view.html', context)


def post_model_create_view(request):
  form = PostModelForm(request.POST or None)
  context = {
    'form': form
  }
  if form.is_valid():
    obj = form.save(commit=False)
    obj.save()
    messages.success(request, 'Created a new blog post!')
    context = {
      'form': PostModelForm()
    }
    return redirect(reverse('djtemp:detail', kwargs={'id': obj.id}))
  return render(request, 'djtemp/create-view.html', context)


def post_model_detail_view(request, id=None):
  obj = get_object_or_404(PostModel, id=id)
  context = {
    'instance': obj,
  }
  return render(request, 'djtemp/detail-view.html', context)


def post_model_update_view(request, id=None):
  obj = get_object_or_404(PostModel, id=id)
  form = PostModelForm(request.POST or None, instance=obj)
  context = {
    'form': form
  }
  if form.is_valid():
    obj = form.save(commit=False)
    obj.save()
    messages.success(request, 'Updated post!')
    return redirect(reverse('djtemp:detail', kwargs={'id': obj.id}))
  return render(request, 'djtemp/update-view.html', context)


def post_model_delete_view(request, id=None):
  obj = get_object_or_404(PostModel, id=id)
  if request.method == 'POST':
    obj.delete()
    messages.success(request, 'Post deleted')
    return redirect(reverse('djtemp:list'))
  context = {
    'object': obj,
  }
  return render(request, 'djtemp/delete-view.html', context)