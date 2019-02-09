from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView

from .models import TVShow

def series_listview(request):
  template_view = 'series/series_list.html'
  queryset = TVShow.objects.all()
  context = {
      "object_list": queryset
  }
  return render(request, template_view, context)