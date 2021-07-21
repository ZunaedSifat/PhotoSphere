from django.contrib import admin
from photos.models import Photo, Tag


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_filter = ('created_at', 'uploader')


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_filter = ('name', 'created_at')
