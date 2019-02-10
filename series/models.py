from django.db import models
from django.conf import settings 
from django.db.models.signals import pre_save, post_save
from .utils import unique_slug_generator
from .validators import validate_name

User = settings.AUTH_USER_MODEL

class TVShow(models.Model):
    user          = models.ForeignKey(User, on_delete=models.CASCADE)
    name          = models.CharField(max_length=120, validators=[validate_name])
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
    slug          = models.SlugField( null=True, blank=True)

    def __str__(self):
      return self.name

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

