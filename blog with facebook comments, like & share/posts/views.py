from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.contrib import messages
from django.utils import timezone
from django.db.models import Q
from .models import Post
from .forms import PostForm

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def list(request):
    # queryset_list = Post.objects.filter(draft=False).filter(publish__lte=timezone.now())#.all() #.order_by('-id')
    # queryset_list = Post.objects.all()
    today = timezone.now().date()
    queryset_list = Post.objects.active()
    if request.user.is_staff or request.user.is_superuser:
        queryset_list = Post.objects.all()
    search_post = request.GET.get('search_post')
    if search_post:
        queryset_list = queryset_list.filter(
            Q(title__icontains=search_post) |
            Q(content__icontains=search_post) |
            Q(user__first_name__icontains=search_post) |
            Q(user__last_name__icontains=search_post)
        ).distinct()
    paginator = Paginator(queryset_list, 2)
    page_request = 'page'
    page = request.GET.get(page_request)
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        queryset = paginator.page(1)
    except EmptyPage:
        queryset = paginator.page(paginator.num_pages)
    context = {
        'objects': queryset,
        'page_request': page_request,
        'today': today
    }
    return render(request, 'index.html', context)


def create(request):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    if not request.user.is_authenticated:
        raise Http404
    if request.method == 'POST':
        form = PostForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            messages.success(request, 'Successfully created!')
            return HttpResponseRedirect(instance.get_absolute_url())
    else:
        form = PostForm()
        # messages.error(request, 'Not successfully created!')
    context = {
        'form': form,
    }
    return render(request, 'form.html', context)


# def detail(request, id):
def detail(request, slug):
    # queryset = get_object_or_404(Post, id=id)
    queryset = get_object_or_404(Post, slug=slug)
    if queryset.draft or queryset.publish > timezone.now().date():
        if not request.user.is_staff or request.user.is_superuser:
            raise Http404
    context = {
        'title': queryset.title,
        'obj': queryset,
    }
    return render(request, 'detail.html', context)


# def update(request, id):
def update(request, slug):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    if not request.user.is_authenticated:
        raise Http404
    # queryset = get_object_or_404(Post, id=id)
    queryset = get_object_or_404(Post, slug=slug)
    # if request.method == 'POST':
    form = PostForm(request.POST or None, request.FILES or None, instance=queryset)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, 'Successfully saved!')
        # messages.success(request, '<a href="#" >Successfully saved!</a>', extra_tags='osama mohamed html_safe')
        # messages.success(request, 'Successfully saved too!')
        return HttpResponseRedirect(instance.get_absolute_url())
    # else:
    #     form = PostForm(instance=queryset)
    #     messages.error(request, 'Not successfully saved!')
    context = {
        'title': queryset.title,
        'obj': queryset,
        'form': form,
    }
    return render(request, 'form.html', context)


# def delete(request, id):
def delete(request, slug):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    if not request.user.is_authenticated:
        raise Http404
    # instance = get_object_or_404(Post, id=id)
    instance = get_object_or_404(Post, slug=slug)
    instance.delete()
    messages.success(request, 'Successfully deleted!')
    return redirect('posts:list')

