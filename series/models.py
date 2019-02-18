from django.db import models
from django.conf import settings 
from django.db.models.signals import pre_save, post_save
from django.urls import reverse 

from .utils import unique_slug_generator
from .validators import validate_name

User = settings.AUTH_USER_MODEL

class TVShow(models.Model):
    user          = models.ForeignKey(User, on_delete=models.CASCADE)
    name          = models.CharField(max_length=200, validators=[validate_name])
    show_id       = models.CharField(max_length=200, null=True, blank=True)
    language      = models.CharField(max_length=200, null=True, blank=True)
    genres        = models.CharField(max_length=200, null=True, blank=True)
    status        = models.CharField(max_length=200, null=True, blank=True)
    runtime       = models.CharField(max_length=150, null=True, blank=True) 
    premiered     = models.CharField(max_length=150, null=True, blank=True) 
    scheduled     = models.CharField(max_length=200, null=True, blank=True) 
    rating        = models.CharField(max_length=150, null=True, blank=True) 
    network       = models.CharField(max_length=150, null=True, blank=True)
    country       = models.CharField(max_length=150, null=True, blank=True)
    image         = models.CharField(max_length=500, null=True, blank=True)
    summary       = models.CharField(max_length=1000, null=True, blank=True)
    nextepisode   = models.CharField(max_length=500, null=True, blank=True)
    created_at    = models.DateTimeField(auto_now_add=True)
    updated_at    = models.DateTimeField(auto_now=True)
    slug          = models.SlugField( null=True, blank=True)

    def __str__(self):
      return self.name

    def get_absolute_url(self):
      return reverse('series:detail', kwargs={'slug': self.slug})
    @property
    def title(self):
      return self.name

def tvshow_pre_save_receiver(sender, instance, *args, **kwargs):
  print('saving..')
  print(instance.created_at)
  if not instance.slug:
    instance.slug = unique_slug_generator(instance)

# def tvshow_post_save_receiver(sender, instance, created, *args, **kwargs):
#   print('saved')
#   print(instance.created_at)
#   if not instance.slug:
#     instance.slug = unique_slug_generator(instance)
#     instance.save()


pre_save.connect(tvshow_pre_save_receiver, sender=TVShow)

# post_save.connect(tvshow_post_save_receiver, sender=TVShow)

