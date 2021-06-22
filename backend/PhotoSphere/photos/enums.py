from django.db.models import TextChoices


class PhotoPrivacyChoices(TextChoices):
    ONLY_ME = 'O', 'Only Me'
    FOLLOWER_ONLY = 'F', 'Follower Only'
    PUBLIC = 'P', 'Public'
