from django.db.models import TextChoices


class OrganizationMemberTypes(TextChoices):
    ADMIN = 'A', 'Admin'
    EDITOR = 'E', 'Editor'
    MODERATOR = 'M', 'Moderator'
