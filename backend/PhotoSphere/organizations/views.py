from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from photos.permissions import ListCreatePermission

from organizations.enums import OrganizationMemberTypes
from organizations.models import Organization, OrganizationMember
from organizations.serializers import OrganizationSerializer
from organizations.permissions import OrganizationDetailsPermission


class OrganizationListCreateAPIView(ListCreateAPIView):
    permission_classes = (ListCreatePermission,)
    serializer_class = OrganizationSerializer
    queryset = Organization.objects.all()

    def perform_create(self, serializer):
        instance = serializer.save()
        instance.members.add(OrganizationMember.objects.create(
            member=self.request.user,
            role=OrganizationMemberTypes.ADMIN
        ))


class OrganizationRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = (OrganizationDetailsPermission, )
    serializer_class = OrganizationSerializer
    queryset = Organization.objects.all()
