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

    def validate(self, attrs):
        print(attrs, self.context)
        attrs = super(OrderSerializer, self).validate(attrs)
        print(attrs.get('user'))
        print(attrs.get('photo').owner.user)

        user = self.context.get('request').user
        if user.id == attrs.get('photo').owner.user.id:
            raise serializers.ValidationError({'user': "Can't buy own photo"})
        if not attrs.get('photo').for_sale:
            raise serializers.ValidationError({'photo': "This photo is not for sale"})

        return attrs
