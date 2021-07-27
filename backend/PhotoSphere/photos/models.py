import string
import os
from PIL import Image, ImageDraw, ImageFont
import urllib

from django.core.files import File
from django.db import models
from django.db.models.signals import pre_save
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from django.conf import settings

from user.models import Profile


User = get_user_model()


class Tag(models.Model):
    name = models.CharField(max_length=32, unique=True)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Tag #{self.name}'


@receiver(pre_save, sender=Tag)
def format_tag_name_handler(sender, instance, *args, **kwargs):
    result = ""
    allowed_chars = string.ascii_letters + string.digits
    for char in instance.name.lower():
        result += char if char in allowed_chars else '-'
    instance.name = result


class Photo(models.Model):
    uploader = models.ForeignKey(to=Profile, on_delete=models.PROTECT, related_name='uploaded_photos', blank=True)
    title = models.CharField(max_length=100)
    caption = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='photos/')

    optimized_image_128 = models.ImageField(upload_to='optimized/', null=True, blank=True)
    optimized_image_256 = models.ImageField(upload_to='optimized/', null=True, blank=True)
    optimized_image_512 = models.ImageField(upload_to='optimized/', null=True, blank=True)
    optimized_image_1024 = models.ImageField(upload_to='optimized/', null=True, blank=True)

    watermarked_optimized_image_128 = models.ImageField(upload_to='watermarked_optimized/', null=True, blank=True)
    watermarked_optimized_image_256 = models.ImageField(upload_to='watermarked_optimized/', null=True, blank=True)
    watermarked_optimized_image_512 = models.ImageField(upload_to='watermarked_optimized/', null=True, blank=True)
    watermarked_optimized_image_1024 = models.ImageField(upload_to='watermarked_optimized/', null=True, blank=True)

    for_sale = models.BooleanField()
    is_digital = models.BooleanField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    created_at = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(to=User, related_name='liked_photos', blank=True)
    like_count = models.IntegerField(default=0)
    tags = models.ManyToManyField(to=Tag, related_name='tagged_photos', blank=True)
    exhibition_entry_count = models.IntegerField(default=0, blank=True)

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


def save_resized_image(instance, image_field, size, add_watermark=False):
    file, ext = os.path.splitext(instance.image.path)
    with Image.open(instance.image.path) as image:
        image.thumbnail(size)
        if add_watermark:
            draw = ImageDraw.Draw(image)
            text = "PhotoSphere.com"
            draw.text((16, 16), text, font=ImageFont.load_default())
        image.save(os.path.join(settings.MEDIA_ROOT, file) + f"_{size}{'w' if add_watermark else 'o'}{ext}", ext[1:])

        image_path = "file://" + os.path.join(settings.MEDIA_ROOT, f"{file}_{size}{'w' if add_watermark else 'o'}{ext}")
        result = urllib.request.urlretrieve(image_path)
        image_field.save(
            os.path.basename(image_path),
            File(open(result[0], 'rb'))
        )
        instance.save()


@receiver(post_save, sender=Photo)
def add_optimized_version(sender, instance, created, **kwargs):
    if created:
        save_resized_image(instance=instance, image_field=instance.optimized_image_128, size=(128, 128))
        save_resized_image(instance=instance, image_field=instance.optimized_image_256, size=(256, 256))
        save_resized_image(instance=instance, image_field=instance.optimized_image_512, size=(512, 512))
        save_resized_image(instance=instance, image_field=instance.optimized_image_1024, size=(1024, 1024))

        save_resized_image(instance=instance, image_field=instance.watermarked_optimized_image_128, size=(128, 128), add_watermark=True)
        save_resized_image(instance=instance, image_field=instance.watermarked_optimized_image_256, size=(256, 256), add_watermark=True)
        save_resized_image(instance=instance, image_field=instance.watermarked_optimized_image_512, size=(512, 512), add_watermark=True)
        save_resized_image(instance=instance, image_field=instance.watermarked_optimized_image_1024, size=(1024, 1024), add_watermark=True)