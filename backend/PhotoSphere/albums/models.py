from django.db import models
from photos.models import Photo
from user.models import Profile


class Album(models.Model):
    owner = models.ForeignKey(to=Profile, related_name='albums', on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    photos = models.ManyToManyField(to=Photo, related_name='albums')
