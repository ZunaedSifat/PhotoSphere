from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save

from user import querysets


UserModel = get_user_model()


class Profile(models.Model):
    user = models.OneToOneField(
        UserModel,
        related_name='profile',
        on_delete=models.CASCADE
    )

    # todo: change this and make different managers for accepted and pending users
    objects = querysets.ProfileQuerySet.as_manager()

    class Meta:
        verbose_name = 'profile'
        verbose_name_plural = 'profiles'
        ordering = ('user', )

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'


def create_profile_model(sender, instance, created, **kwargs):
    if created:
        profile = Profile(user=instance)
        profile.save()


post_save.connect(create_profile_model, sender=UserModel)
