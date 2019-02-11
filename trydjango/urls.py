"""trydjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
from django.views.generic import TemplateView, ListView, DetailView, CreateView
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LoginView.as_view(), name='logout'),
    path('password_change/', LoginView.as_view(), name='password_change'),
    path('password_change/done/', LoginView.as_view(), name='password_change_done'),
    path('password_reset/', LoginView.as_view(), name='password_reset'),
    path('password_reset/done/', LoginView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', LoginView.as_view(), name='password_reset_confirm'),
    path('reset/done/', LoginView.as_view(), name='password_reset_complete'),

    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('series/', include('series.urls', namespace='series')),
    path('profiles/', include('profiles.urls', namespace='profiles')),
    path('about/', TemplateView.as_view(template_name='about.html'), name='about'),
    path('contact/', TemplateView.as_view(template_name='contact.html'), name='contact'),
]