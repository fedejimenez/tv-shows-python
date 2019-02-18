import logging, sys
import json

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView

from .models import TVShow
from .forms import SeriesCreateForm, TVShowCreateForm


class SeriesListView(LoginRequiredMixin, ListView):
  def get_queryset(self):
    return TVShow.objects.filter(user=self.request.user)

class SeriesDetailView(LoginRequiredMixin, DetailView):
  def get_queryset(self):
    return TVShow.objects.filter(user=self.request.user)

class SeriesCreateView(LoginRequiredMixin, CreateView):
  form_class = TVShowCreateForm
  login_url = '/login/' # It can be changed
  template_name = 'form.html'

  def form_valid(self, form):
    instance = form.save(commit=False)
    instance.user = self.request.user
    return super(SeriesCreateView, self).form_valid(form)

  def get_context_data(self, *args, **kwargs):
    context = super(SeriesCreateView, self).get_context_data(*args, **kwargs)
    context['title'] = 'Add a Series'
    return context

class SeriesUpdateView(LoginRequiredMixin, UpdateView):
  form_class = TVShowCreateForm
  login_url = '/login/' # It can be changed
  template_name = 'form.html'

  def get_context_data(self, *args, **kwargs):
    context = super(SeriesUpdateView, self).get_context_data(*args, **kwargs)
    name = self.get_object().name  
    context['title'] = f'Update {name}'
    return context

  def get_queryset(self):
    return TVShow.objects.filter(user=self.request.user)
