from django.contrib.auth import get_user_model
from rest_framework import serializers
from user.models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(source='user.id', required=False)
    email = serializers.EmailField(source='user.email', required=False)
    first_name = serializers.CharField(source='user.first_name', required=False)
    last_name = serializers.CharField(source='user.last_name', required=False)

    class Meta:
        model = Profile
        fields = (
            'id', 'email', 'first_name', 'last_name', 'avatar'
        )
        read_only_fields = ['id']

    def validate(self, attrs):
        return attrs

    def create(self, validated_data):
        raise Exception("ProfileSerializer can't be called to create objects")

    def update(self, instance, validated_data):
        """ Updates the object in database from validated data """
        instance.avatar = validated_data.get('avatar', None)
        instance.save()

        # updating and saving User attribute
        user = validated_data.get('user', None)
        if user:
            instance.user.first_name = user.get('first_name', instance.user.first_name)
            instance.user.last_name = user.get('last_name', instance.user.last_name)
            instance.user.save()

        return instance


class ProfileCreationSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(source='user.id', read_only=True)
    email = serializers.EmailField(source='user.email', required=True)
    first_name = serializers.CharField(source='user.first_name', required=True)
    last_name = serializers.CharField(source='user.last_name', required=True)
    password = serializers.CharField(
        write_only=True,
        required=True,
        style={'input_type': 'password'}
    )

    class Meta:
        model = Profile
        fields = (
            'id', 'email', 'first_name', 'last_name', 'password',  'avatar'
        )
        read_only_fields = ['id']

    def validate(self, attrs):
        email = attrs.get('user').get('email')
        if get_user_model().objects.filter(username=email).exists():
            raise serializers.ValidationError({'email': 'Email already exists'})

        return attrs

    def create(self, validated_data):
        user = get_user_model().objects.create_user(
            username=validated_data.get('user').get('email'),
            email=validated_data.get('user').get('email'),
            first_name=validated_data.get('user').get('first_name'),
            last_name=validated_data.get('user').get('last_name'),
            password=validated_data.get('password')
        )
        return user.profile

    def update(self, instance, validated_data):
        raise Exception("ProfileCreationSerializer can't be called to update objects")
