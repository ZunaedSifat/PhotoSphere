# Generated by Django 3.2.3 on 2021-06-19 09:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='album',
            old_name='profile',
            new_name='owner',
        ),
    ]
