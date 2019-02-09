from django.db import models

# Create your models here.
class TVShow(models.Model):
    name          = models.CharField(max_length=120)
    imdb          = models.CharField(max_length=120, null=True, blank=True) 
    summary       = models.CharField(max_length=500, null=True, blank=True)
    status        = models.CharField(max_length=500, null=True, blank=True)
    genres        = models.CharField(max_length=500, null=True, blank=True)
    premiered     = models.CharField(max_length=500, null=True, blank=True)
    scheduled     = models.CharField(max_length=500, null=True, blank=True)
    seasons       = models.CharField(max_length=500, null=True, blank=True)
    episodes      = models.CharField(max_length=500, null=True, blank=True)
    reviews       = models.CharField(max_length=500, null=True, blank=True)
    created_at    = models.DateTimeField(auto_now_add=True)
    updated_at    = models.DateTimeField(auto_now=True)

    def __str__(self):
      return self.name