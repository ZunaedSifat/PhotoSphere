from rest_framework import serializers
from albums.models import Album


class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ['id', 'owner', 'name', 'description', 'photos', 'created_at']
        read_only_fields = ['id', 'created_at', 'owner']
