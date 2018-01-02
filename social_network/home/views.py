from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import HomeForm
from .models import Post, Friend

# def home(request):
#     return render(request, 'home/home.html')


class Home(TemplateView):
    template_name = 'home/home.html'

    def get(self, request):
        form = HomeForm()
        posts = Post.objects.all().order_by('-id')
        users = User.objects.exclude(id=request.user.id)
        friend = Friend.objects.get(current_user=request.user)
        friends = friend.users.all()
        args = {'form': form,
                'posts': posts,
                'users': users,
                'friends': friends
                }
        return render(request, self.template_name, args)

    def post(self, request):
        form = HomeForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            text = form.cleaned_data['post']
            return redirect('home:home')
        args = {'form': form}
        return render(request, self.template_name, args)


def change_friends(request, friendship, id):
    friend = User.objects.get(id=id)
    if friendship == 'add':
        Friend.add_friend(request.user, friend)
    elif friendship == 'remove':
        Friend.remove_friend(request.user, friend)
    return redirect('home:home')
