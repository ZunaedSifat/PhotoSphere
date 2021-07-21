from django.db import models
from organizations.models import Organization
from photos.models import Photo


class Exhibition(models.Model):
    organizer = models.ForeignKey(to=Organization, on_delete=models.PROTECT, related_name='exhibitions')
    title = models.CharField(max_length=255)
    description = models.TextField()
    avatar = models.ImageField(upload_to='exhibition/', null=True, blank=True)
    entry_fee = models.DecimalField(max_digits=6, decimal_places=2)
    # privacy = models.TextField(max_length=1, ) todo: add

    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        return f'{self.title} by {self.organizer}'


class ExhibitionEntry(models.Model):
    exhibition = models.ForeignKey(to=Exhibition, on_delete=models.CASCADE, related_name='entries')
    photo = models.ForeignKey(to=Photo, on_delete=models.PROTECT, related_name='exhibition_entries')
    for_sale = models.BooleanField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        return f'{self.photo.title} at {self.exhibition.title}'

    class Meta:
        ordering = ('order', )
