from django.http import HttpResponse

import os

def home_view(request):
  HTML_STRING = f"""
  <h1>Hi {os.getlogin()}!</h1>
  """
  return HttpResponse(HTML_STRING)