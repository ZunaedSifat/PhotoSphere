from rest_framework import serializers
from organizations.models import Organization, OrganizationMember


class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = ('id', 'name', 'description', 'avatar', 'website', 'members', 'created_at')
        read_only_fields = ('id', 'created_at')


class OrganizationMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrganizationMember
        fields = ('id', 'organization', 'member', 'role', 'updated_at')
        read_only_fields = ('id', 'updated_at')
