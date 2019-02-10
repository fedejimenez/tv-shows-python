import logging, sys
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, CreateView

from .models import TVShow
from .forms import SeriesCreateForm, TVShowCreateForm

def series_createview(request):
  form = TVShowCreateForm(request.POST or None)
  errors = None
  if form.is_valid():
    form.save()
    return HttpResponseRedirect("/series/")
  if form.errors:
      errors = form.errors
  template_name = 'series/form.html'
  context = {"form": form, "errors": errors}
  return render(request, template_name, context)

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

class SeriesCreateView(CreateView):
  form_class = TVShowCreateForm
  template_name = 'series/form.html'
  success_URL = "/series/" 