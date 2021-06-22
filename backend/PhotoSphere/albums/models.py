from django.db import models
from photos.enums import PhotoPrivacyChoices
from photos.models import Photo
from user.models import Profile


class Album(models.Model):
    owner = models.ForeignKey(to=Profile, related_name='albums', on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    description = models.TextField()
    privacy = models.CharField(
        max_length=1,
        choices=PhotoPrivacyChoices.choices,
        default=PhotoPrivacyChoices.ONLY_ME,
        blank=False
    )
    created_at = models.DateTimeField(auto_now=True)
    photos = models.ManyToManyField(to=Photo, related_name='albums')
