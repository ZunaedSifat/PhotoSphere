# Generated by Django 3.2.3 on 2021-07-25 20:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exhibitions', '0004_auto_20210721_2159'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exhibitionentry',
            name='for_sale',
        ),
        migrations.RemoveField(
            model_name='exhibitionentry',
            name='price',
        ),
    ]
