from django.db import models
from django.contrib.auth import get_user_model
from organizations.enums import OrganizationMemberTypes
from django.core.validators import ValidationError



class OrganizationMember(models.Model):
    member = models.ForeignKey(to=get_user_model(), on_delete=models.PROTECT, related_name='membership')
    role = models.TextField(
        max_length=1,
        choices=OrganizationMemberTypes.choices,
        default=OrganizationMemberTypes.MODERATOR
    )
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.member}, {self.role}'


class Organization(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    avatar = models.ImageField(upload_to='org/avatar/', null=True, blank=True)
    website = models.URLField()
    members = models.ManyToManyField(to=OrganizationMember, related_name='organizations', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f'Organization {self.name}'

    def clean(self, *args, **kwargs):
        for item_a in self.members.all():
            for item_b in self.members.all():
                if item_a.pk != item_b.pk and item_a.member.id == item_b.member.id:
                    raise ValidationError({'members': 'Multiple OrganizationMember with same member given.'})

        super(Organization, self).clean(*args, **kwargs)

    def save(self, *args, **kwargs):
        self.full_clean()
        super(Organization, self).save(*args, **kwargs)
