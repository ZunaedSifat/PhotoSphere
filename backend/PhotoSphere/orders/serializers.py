from rest_framework import serializers
from orders.models import Order


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = (
            'id',
            'transaction_id',
            'photo',
            'user',
            'phone',
            'address',
            'city',
            'is_paid',
            'created_at',
            'redirection_url'
        )
        read_only_fields = ('id', 'transaction_id', 'is_paid', 'created_at', 'valid_till', 'redirection_url')