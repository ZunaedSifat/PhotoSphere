from rest_framework import serializers
from exhibitions.models import Exhibition, ExhibitionEntry


class ExhibitionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exhibition
        fields = ('id', 'organizer', 'title', 'description', 'avatar', 'entry_fee', 'start_date', 'end_date', 'created_at', 'updated_at')
        read_only_fields = ('id', 'created_at', 'updated_at')


class ExhibitionEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = ExhibitionEntry
        fields = ('id', 'exhibition', 'photo', 'for_sale', 'price', 'order', 'created_at', 'updated_at')
        read_only_fields = ('id', 'created_at', 'updated_at')
