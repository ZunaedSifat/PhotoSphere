# Generated by Django 3.2.3 on 2021-07-21 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organizations', '0003_alter_organization_members'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organization',
            name='members',
            field=models.ManyToManyField(blank=True, related_name='organizations', to='organizations.OrganizationMember'),
        ),
    ]
