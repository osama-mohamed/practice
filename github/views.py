from django.shortcuts import render
import requests

from .forms import UserForm

URL = 'https://api.github.com/users/{}'


def user_data(api_data):
    temporary_dict = {}
    temporary_dict['login'] = api_data['login']
    temporary_dict['public_repos'] = api_data['public_repos']
    temporary_dict['followers'] = api_data['followers']
    temporary_dict['following'] = api_data['following']
    temporary_dict['name'] = api_data['name']
    temporary_dict['url'] = api_data['url']
    temporary_dict['repos_url'] = api_data['repos_url']
    temporary_dict['html_url'] = api_data['html_url']
    temporary_dict['id'] = api_data['id']
    return temporary_dict


def home(request):
    user_one_stats = {}
    user_two_stats = {}
    form = UserForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        user_one = form.cleaned_data.get('user_name_one')
        user_two = form.cleaned_data.get('user_name_two')
        user_one_result = requests.get(URL.format(user_one)).json()
        user_one_stats = user_data(user_one_result)
        user_two_result = requests.get(URL.format(user_two)).json()
        user_two_stats = user_data(user_two_result)
    context = {
        'user_one': user_one_stats,
        'user_two': user_two_stats,
        'form': form,
    }
    return render(request, 'index.html', context)




# form = CommentForm(request.POST or None, initial=initial_data)
# if form.is_valid() and request.user.is_authenticated():
#    obj_id = form.cleaned_data.get('object_id')