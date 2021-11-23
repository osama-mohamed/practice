from django.http import HttpResponse

from articles.models import Article

def home_view(request):
  article_obj = Article.objects.get(id=1)
  HTML_STRING = f"""
  <h1>#{article_obj.id}: {article_obj.title} !</h1>
  <p>Hi {article_obj.content}!</p>
  """
  return HttpResponse(HTML_STRING)