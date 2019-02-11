from .views import ProfileDetailView
from django.urls import path

app_name = 'profiles'

urlpatterns = [
    path('<username>', ProfileDetailView.as_view(), name='detail'),
]