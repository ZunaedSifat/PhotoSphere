# Generated by Django 3.2.3 on 2021-07-27 18:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0019_photo_exhibition_entry_count'),
    ]

    operations = [
        migrations.RenameField(
            model_name='photo',
            old_name='uploader',
            new_name='owner',
        ),
    ]
