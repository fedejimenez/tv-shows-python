import logging, sys
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, CreateView

from .models import TVShow
from .forms import SeriesCreateForm, TVShowCreateForm

# Function Based View
@login_required(login_url='/login/') # Decorator: functions taht wraps another function (this ons is built-in)
def series_createview(request):
  form = TVShowCreateForm(request.POST or None)
  errors = None
  if form.is_valid():
    # if request.user.is_authenticated():
      # instance = form.save(commit=False)
      # instance.user = request.user
      # instance.save()
      return HttpResponseRedirect("/series/")
    # else:
      # return HttpResponseRedirect("/login/")
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


# Class Based View
class SeriesCreateView(LoginRequiredMixin, CreateView):
  form_class = TVShowCreateForm
  login_url = '/login/' # It can be changed
  template_name = 'series/form.html'
  success_url = "/series/" 

  def form_valid(self, form):
    instance = form.save(commit=False)
    instance.user = self.request.user
    return super(SeriesCreateView, self).form_valid(form)
