from django.urls import path, re_path

from .views import (
  SeriesListView,
  SeriesDetailView,
  SeriesCreateView,
  SeriesUpdateView
)

app_name = 'series'

urlpatterns = [
    path('', SeriesListView.as_view(), name='list'),
    path('create', SeriesCreateView.as_view(), name='create'),
    path('<slug>', SeriesDetailView.as_view(), name='detail'),
    path('<slug>/edit', SeriesUpdateView.as_view(), name='edit'),
]