from django.http import HttpResponse, HttpResponseRedirect


def redirect_somewhere(request):
  return HttpResponseRedirect('/some/path/')