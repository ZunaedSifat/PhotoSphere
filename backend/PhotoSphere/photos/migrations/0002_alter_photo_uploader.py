# Generated by Django 3.2.3 on 2021-06-09 03:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_profile_avatar'),
        ('photos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='uploader',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, related_name='uploaded_photos', to='user.profile'),
        ),
    ]