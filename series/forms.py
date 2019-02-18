from django import forms
from .models import TVShow 
from .validators import validate_name

from django.conf import settings
import requests

class SeriesCreateForm(forms.Form):
  name          = forms.CharField()
  language      = forms.CharField(required=False)
  genres        = forms.CharField(required=False)
  status        = forms.CharField(required=False)
  runtime       = forms.CharField(required=False) 
  show_id       = forms.CharField(required=False)
  premiered     = forms.CharField(required=False) 
  scheduled     = forms.CharField(required=False) 
  rating        = forms.CharField(required=False) 
  network       = forms.CharField(required=False)
  country       = forms.CharField(required=False)
  image         = forms.CharField(required=False)
  summary       = forms.CharField(required=False)
  nextepisode   = forms.CharField(required=False)

  def clean_name(self):
    name = self.cleaned_data.get('name')
    if name == "":
       raise form.ValidationError("Name must be complete")
    return name

  def clean_genres(self):
    genres = self.cleaned_data.get('genres')
    return genres

class TVShowCreateForm(forms.ModelForm):
  class Meta:
    model = TVShow
    fields = [
      'name',          
      'language',      
      'genres',        
      'status',        
      'runtime',        
      'show_id',       
      'premiered',      
      'scheduled',      
      'rating',         
      'network',       
      'country',       
      'image',         
      'summary',       
      'nextepisode',   
    ]    

  def clean_name(self):
    name = self.cleaned_data.get('name')
    if name == "":
       raise form.ValidationError("Name must be complete")
    return name

  def clean_genres(self):
    genres = self.cleaned_data.get('genres')
    return genres
