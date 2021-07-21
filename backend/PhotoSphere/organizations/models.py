from django.db import models
from django.contrib.auth import get_user_model
from organizations.enums import OrganizationMemberTypes


class Organization(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    avatar = models.ImageField(upload_to='org/avatar/', null=True, blank=True)
    website = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Organization {self.name}'


class OrganizationMember(models.Model):
    organization = models.ForeignKey(to=Organization, on_delete=models.CASCADE, related_name='members')
    member = models.ForeignKey(to=get_user_model(), on_delete=models.PROTECT, related_name='membership')
    role = models.TextField(
        max_length=1,
        choices=OrganizationMemberTypes.choices,
        default=OrganizationMemberTypes.MODERATOR
    )
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('organization', 'member')
        # todo: send validation error instead of 503

    def __str__(self):
        return f'{self.member}, {self.role} at {self.organization}'
