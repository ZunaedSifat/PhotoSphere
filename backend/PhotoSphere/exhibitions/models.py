from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from organizations.models import Organization
from photos.models import Photo


class Exhibition(models.Model):
    organizer = models.ForeignKey(to=Organization, on_delete=models.PROTECT, related_name='exhibitions')
    title = models.CharField(max_length=255)
    description = models.TextField()
    avatar = models.ImageField(upload_to='exhibition/', null=True, blank=True)
    entry_fee = models.DecimalField(max_digits=6, decimal_places=2)

    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        return f'{self.title} by {self.organizer}'


class ExhibitionEntry(models.Model):
    exhibition = models.ForeignKey(to=Exhibition, on_delete=models.CASCADE, related_name='entries')
    photo = models.ForeignKey(to=Photo, on_delete=models.PROTECT, related_name='exhibition_entries')
    order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        return f'{self.photo.title} at {self.exhibition.title}'

    class Meta:
        ordering = ('order', )


@receiver(post_save, sender=ExhibitionEntry)
def add_optimized_version(sender, instance, created, **kwargs):
    instance.photo.exhibition_entry_count = instance.photo.exhibition_entries.count()
    instance.photo.save()


class Theme(models.Model):
    GRID = 'G'
    CAROUSEL = 'C'
    LAYOUT_CHOICES = (
        (GRID, 'Grid'),
        (CAROUSEL, 'Carousel')
    )

    background_color = models.CharField(max_length=7)
    frame_radius = models.FloatField()
    frame_color = models.CharField(max_length=7)
    frame_padding = models.IntegerField()
    column = models.IntegerField()
    layout = models.CharField(max_length=1, choices=LAYOUT_CHOICES)
