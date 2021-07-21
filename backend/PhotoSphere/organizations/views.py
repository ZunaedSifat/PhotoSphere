from rest_framework.generics import ListCreateAPIView
from photos.permissions import ListCreatePermission

from organizations.enums import OrganizationMemberTypes
from organizations.models import Organization, OrganizationMember
from organizations.serializers import OrganizationSerializer


class OrganizationListCreateAPIView(ListCreateAPIView):
    permission_classes = (ListCreatePermission,)
    serializer_class = OrganizationSerializer
    queryset = Organization.objects.all()

    def perform_create(self, serializer):
        instance = serializer.save()
        instance.members.add(OrganizationMember.objects.create(
            member=self.request.user,
            role=OrganizationMemberTypes.EDITOR
        ))
