from django.contrib import admin
from photos.models import Photo


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_filter = ('created_at', 'uploader')
