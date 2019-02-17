from django import forms
from .models import TVShow 
from .validators import validate_name

from django.conf import settings
import requests

class SeriesCreateForm(forms.Form):
  name          = forms.CharField()
  summary       = forms.CharField(required=False)
  rating        = forms.CharField(required=False)
  status        = forms.CharField(required=False)

  def clean_name(self):
    name = self.cleaned_data.get('name')
    if name == "":
       raise form.ValidationError("Name must be complete")
    return name

class TVShowCreateForm(forms.ModelForm):
  class Meta:
    model = TVShow
    fields = [
      'name', 
      'summary', 
      'rating', 
      'status'
    ]    

  def clean_name(self):
    name = self.cleaned_data.get('name')
    if name == "":
       raise form.ValidationError("Name must be complete")
    return name
