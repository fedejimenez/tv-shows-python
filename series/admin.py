from django.contrib import admin

# Register your models here.
from .models import TVShow, Genre

admin.site.register(TVShow)
admin.site.register(Genre)