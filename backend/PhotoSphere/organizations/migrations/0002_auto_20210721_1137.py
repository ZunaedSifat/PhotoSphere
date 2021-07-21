# Generated by Django 3.2.3 on 2021-07-21 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organizations', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='organization',
            name='members',
        ),
        migrations.AddField(
            model_name='organization',
            name='members',
            field=models.ManyToManyField(related_name='organizations', to='organizations.OrganizationMember'),
        ),
    ]