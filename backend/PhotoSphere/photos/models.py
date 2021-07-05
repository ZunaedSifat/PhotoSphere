from django.db import models
from user.models import Profile
from photos.enums import PhotoPrivacyChoices
from django.contrib.auth import get_user_model

User = get_user_model()

class Photo(models.Model):
    uploader = models.ForeignKey(to=Profile, on_delete=models.PROTECT, related_name='uploaded_photos', blank=True)
    title = models.CharField(max_length=100)
    caption = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='photos/')
    privacy = models.CharField(
        max_length=1,
        choices=PhotoPrivacyChoices.choices,
        default=PhotoPrivacyChoices.ONLY_ME,
        blank=False
    )
    for_sale = models.BooleanField()
    is_digital = models.BooleanField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    created_at = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(to=User, related_name='liked_photos')
    like_count = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    def add_like(self, user):
        assert isinstance(user, User)
        self.likes.add(user)
        self.like_count = self.likes.all().count()
        self.save()

    def remove_like(self, user):
        assert isinstance(user, User)
        self.likes.remove(user)
        self.like_count = self.likes.all().count()
        self.save()
