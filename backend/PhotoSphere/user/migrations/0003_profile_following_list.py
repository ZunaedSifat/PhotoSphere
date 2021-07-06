# Generated by Django 3.2.3 on 2021-07-04 06:29

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user', '0002_profile_avatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='following_list',
            field=models.ManyToManyField(related_name='follower_list', to=settings.AUTH_USER_MODEL),
        ),
    ]
