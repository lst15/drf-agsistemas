from django.template import loader
from django.http import HttpResponse

def pages(request):
  context = {}
  html_template = loader.get_template('page-404.html')
  return HttpResponse(html_template.render(context, request))
