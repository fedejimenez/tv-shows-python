import logging, sys
from django.shortcuts import render, get_object_or_404
from django.views import View

from .forms import DictionaryForm
 
def home(request):
  search_result = {}
  if 'name' in request.GET:
      form = DictionaryForm(request.GET)
      if form.is_valid():
          search_result = form.search()
  else:
      form = DictionaryForm()
  print(search_result)
  return render(request, 'home.html', {'form': form, 'search_result': search_result})