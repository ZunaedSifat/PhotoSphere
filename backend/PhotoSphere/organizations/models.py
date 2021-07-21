from django.db import models
from django.contrib.auth import get_user_model
from organizations.enums import OrganizationMemberTypes


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
    members = models.ManyToManyField(to=OrganizationMember, related_name='organizations', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Organization {self.name}'

    # todo: add validation to make sure that one person is not duplicated in the members list

