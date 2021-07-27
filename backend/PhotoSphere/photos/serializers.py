from rest_framework import serializers
from photos.models import Photo, Tag


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = (
            'id',
            'uploader',
            'title',
            'caption',
            'tags',
            'image',
            'for_sale',
            'is_digital',
            'price',
            'created_at',
            'like_count'
        )
        read_only_fields = ['id']


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('id', 'name', 'description')
        read_only_fields = ['id']