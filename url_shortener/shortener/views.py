from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.views import View
from .models import URL
from .forms import SubmitUrlForm
from analytics.models import ClickEvent


class HomeView(View):
    def get(self, request, *args, **kwargs):
        form = SubmitUrlForm()
        context = {
            'title': 'OSAMA MOHAMED',
            'title2': 'SHORTEN SERVICES',
            'form': form
        }
        return render(request, 'shortener/home.html', context)

    def post(self, request, *args, **kwargs):
        # print(request.POST)
        # print(request.POST['url'])
        # print(request.POST.get('url'))
        # print(cleaned_data.get('url'))
        # print(cleaned_data['url'])
        form = SubmitUrlForm(request.POST)
        context = {
            'title': 'OSAMA MOHAMED SAHORTENER SERVICES',
            'form': form
        }
        template = 'shortener/home.html'
        if form.is_valid():
            new_url = form.cleaned_data.get('url')
            obj, created = URL.objects.get_or_create(url=new_url)
            context = {
                'object': obj,
                'created': created
            }
            if created:
                template = 'shortener/success.html'
            else:
                template = 'shortener/already_exists.html'

        return render(request, template, context)


class RedirectView(View):
    def get(self, request, shortcode=None, *args, **kwargs):
        qs = URL.objects.filter(shortcode__iexact=shortcode)
        if qs.count() and qs.exists():
            obj = qs.first()
            ClickEvent.objects.create_event(obj)
            return HttpResponseRedirect(obj.url)
            # obj = get_object_or_404(URL, shortcode=shortcode)
            # ClickEvent.objects.create_event(obj)
            # return HttpResponseRedirect(obj.url)
        else:
            raise Http404




# def redirect_view(request, shortcode=None, *args, **kwargs):
#     obj = get_object_or_404(URL, shortcode=shortcode)
#     return HttpResponseRedirect(obj.url)

    # qs = URL.objects.filter(shortcode__iexact=shortcode.upper())
    # obj_url = None
    # if qs.exists() and qs.count() == 1:
    #     obj = qs.first()
    #     obj_url = obj.url
    # return HttpResponse('func : {sc}'.format(sc=obj_url))
