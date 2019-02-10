from django.urls import path, re_path

from .views import (
  TVShowListView,
  TVShowDetailView,
  SeriesCreateView
)

app_name = 'series'

urlpatterns = [
    path('', TVShowListView.as_view(), name='list'),
    path('create', SeriesCreateView.as_view(), name='create'),
    path('<slug>', TVShowDetailView.as_view(), name='detail'),
]