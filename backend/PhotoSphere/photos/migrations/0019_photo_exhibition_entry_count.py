# Generated by Django 3.2.3 on 2021-07-27 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0018_auto_20210727_1627'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='exhibition_entry_count',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
