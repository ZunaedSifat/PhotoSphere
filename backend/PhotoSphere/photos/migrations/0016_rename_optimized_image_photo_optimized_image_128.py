# Generated by Django 3.2.3 on 2021-07-27 15:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0015_alter_photo_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='photo',
            old_name='optimized_image',
            new_name='optimized_image_128',
        ),
    ]