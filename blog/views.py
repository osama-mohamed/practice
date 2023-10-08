from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages

from django.db.models import Q


from .forms import PostModelForm
from .models import PostModel



def post_model_robust_view(request, id=None):
  context = {}
  if id is None:
    template = 'blog/robust_list_view.html'
    context['object_list'] = PostModel.objects.all()
  else:
    obj = get_object_or_404(PostModel, id=id)
    context['object'] = obj
    template = 'blog/robust_detail_view.html'
    if 'create' in request.get_full_path():
      template = 'blog/robust_create_view.html'
      success_message = 'Created successfully!'
    if 'update' in request.get_full_path():
      template = 'blog/robust_update_view.html'
      success_message = 'Updated successfully!'
    if 'create' or 'update' in request.get_full_path():
      form = PostModelForm(request.POST or None, instance=obj)
      context['form'] = form
      if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        messages.success(request, success_message)
        return redirect('blog:robust_detail', id=obj.id)
    if 'delete' in request.get_full_path():
      template = 'blog/robust_delete_view.html'
      if request.method == 'POST':
        obj.delete()
        messages.success(request, 'Deleted successfully!')
        return redirect('blog:robust_list')
  return render(request, template, context)




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
  q = request.GET.get('q', None)
  qs = PostModel.objects.all()
  if q is not None:
    # qs = qs.filter(title__icontains=q)
    qs = qs.filter(
      Q(title__icontains=q) |
      Q(content__icontains=q)
    )
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


