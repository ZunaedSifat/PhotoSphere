from rest_framework import serializers
from photos.models import Photo


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ('id', 'uploader', 'title', 'caption', 'image', 'for_sale', 'is_digital', 'price')
        read_only_fields = ['id']
