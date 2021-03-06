# Generated by Django 3.2.3 on 2021-07-27 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0012_remove_photo_privacy'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='optimized',
            field=models.ImageField(blank=True, null=True, upload_to='photos/optimized/'),
        ),
        migrations.AddField(
            model_name='photo',
            name='optimized_watermarked',
            field=models.ImageField(blank=True, null=True, upload_to='photos/optimized_watermarked/'),
        ),
        migrations.AddField(
            model_name='photo',
            name='watermarked',
            field=models.ImageField(blank=True, null=True, upload_to='photos/optimized/'),
        ),
    ]
