# Generated by Django 3.2.3 on 2021-07-27 05:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0011_alter_photo_likes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='privacy',
        ),
    ]