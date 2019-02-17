import logging, sys
from django.shortcuts import render, get_object_or_404
from django.views import View

from .forms import DictionaryForm
import random

def home(request):
  search_result = {}
  id = random.randint(1,41014)
  if(request.GET.get('btn-random')):
     search_result = DictionaryForm.search((request.GET.get('id')) )
     print (search_result)
  else:
      form = DictionaryForm()

  if 'name' in request.GET:
      form = DictionaryForm(request.GET)
      if form.is_valid():
          search_result = form.search()
      print(search_result['id'])
  else:
      form = DictionaryForm()
  return render(request, 'home.html', {'form': form, 'search_result': search_result})
