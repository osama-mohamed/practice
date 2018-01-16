from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.contrib import messages
from django.utils import timezone
from django.db.models import Q
from .models import Post
from .forms import PostForm
from comments.forms import CommentForm

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from comments.models import Comment
from django.contrib.contenttypes.models import ContentType
# from .utils import get_read_time


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
    paginator = Paginator(queryset_list, 10)
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
        if not request.user.is_staff or not request.user.is_superuser:
            raise Http404
    # content_type = ContentType.objects.get_for_model(Post)
    # object_id = queryset.id
    # # Post.objects.get(id=queryset.id)
    # comments = Comment.objects.filter(content_type=content_type, object_id=object_id)
    # comments = Comment.objects.filter_by_queryset(queryset)
    comments = queryset.comments
    # print(get_read_time(queryset.content))
    # print(get_read_time(queryset.get_markdown()))
    initial_data = {
        'content_type': queryset.get_content_type,
        'object_id': queryset.id,
    }
    form = CommentForm(request.POST or None, initial=initial_data)
    if form.is_valid() and request.user.is_authenticated():
        c_type = form.cleaned_data.get('content_type')
        content_type = ContentType.objects.get(model=c_type)
        obj_id = form.cleaned_data.get('object_id')
        content_data = form.cleaned_data.get('content')
        parent_obj = None
        try:
            parent_id = int(request.POST.get('parent_id'))
        except:
            parent_id = None
        if parent_id:
            parent_qs = Comment.objects.filter(id=parent_id)
            if parent_qs.exists() and parent_qs.count() == 1:
                parent_obj = parent_qs.first()
        new_comment, created = Comment.objects.get_or_create(
            user=request.user,
            content_type=content_type,
            object_id=obj_id,
            content=content_data,
            parent=parent_obj
        )
        return HttpResponseRedirect(new_comment.content_object.get_absolute_url())
    context = {
        'title': queryset.title,
        'obj': queryset,
        'comments': comments,
        'comment_form': form,
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

