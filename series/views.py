import logging, sys
from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView

from .models import TVShow

def series_listview(request):
  template_name = 'series/series_list.html'
  queryset = TVShow.objects.all()
  context = {
      "object_list": queryset
  }
  return render(request, template_name, context)

class TVShowListView(ListView):
  def get_queryset(self):
      slug = self.kwargs.get('name')
      if slug: 
        queryset = TVShow.objects.filter(
          Q(name__iexact=slug) |
          Q(name__icontains=slug) 
        )
      else:
        queryset = TVShow.objects.all()
      return queryset

class TVShowDetailView(DetailView):
  queryset = TVShow.objects.all()

  # def get_object(self, *args, **kwargs):
  #   tvshow_id = self.kwargs.get('tvshow_id')
  #   obj = get_object_or_404(TVShow, id=tvshow_id) #pk = tvshow_id
  #   return obj