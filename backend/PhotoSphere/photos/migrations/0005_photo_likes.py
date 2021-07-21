# Generated by Django 3.2.3 on 2021-07-05 05:17

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('photos', '0004_photo_privacy'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='likes',
            field=models.ManyToManyField(related_name='liked_photos', to=settings.AUTH_USER_MODEL),
        ),
    ]