# Generated by Django 3.2.3 on 2021-07-21 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0009_alter_photo_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='tagged_photos', to='photos.Tag'),
        ),
    ]
