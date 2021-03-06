from rest_framework import serializers
from photos.models import Photo, Tag


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = (
            'id',
            'owner',
            'title',
            'caption',
            'tags',
            'image',
            'optimized_image_128',
            'optimized_image_256',
            'optimized_image_512',
            'optimized_image_1024',
            'watermarked_optimized_image_128',
            'watermarked_optimized_image_256',
            'watermarked_optimized_image_512',
            'watermarked_optimized_image_1024',
            'for_sale',
            'is_digital',
            'price',
            'created_at',
            'likes',
            'like_count',
            'exhibition_entry_count'
        )
        read_only_fields = [
            'id',
            'likes',
            'optimized_image_128',
            'optimized_image_256',
            'optimized_image_512',
            'optimized_image_1024'
            'watermarked_optimized_image_128',
            'watermarked_optimized_image_256',
            'watermarked_optimized_image_512',
            'watermarked_optimized_image_1024',
            'exhibition_entry_count',
        ]


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('id', 'name', 'description')
        read_only_fields = ['id']