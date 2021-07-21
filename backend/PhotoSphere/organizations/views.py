from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from photos.permissions import ListCreatePermission

from organizations.enums import OrganizationMemberTypes
from organizations.models import Organization, OrganizationMember
from organizations.serializers import OrganizationSerializer, OrganizationMemberSerializer
from organizations.permissions import OrganizationDetailsPermission, OrganizationMemberPermission


class OrganizationListCreateAPIView(ListCreateAPIView):
    permission_classes = (ListCreatePermission,)
    serializer_class = OrganizationSerializer
    queryset = Organization.objects.all()

    def perform_create(self, serializer):
        instance = serializer.save()
        OrganizationMember.objects.create(
            member=self.request.user,
            role=OrganizationMemberTypes.ADMIN,
            organization=instance
        )


class OrganizationRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = (OrganizationDetailsPermission, )
    serializer_class = OrganizationSerializer
    queryset = Organization.objects.all()


class OrganizationMemberListCreateAPIView(ListCreateAPIView):
    permission_classes = (OrganizationMemberPermission, )
    serializer_class = OrganizationMemberSerializer
    queryset = OrganizationMember.objects.all()

    def filter_queryset(self, queryset):
        try:
            organization_id = int(self.request.query_params.get('organization'))
            queryset = queryset.filter(organization_id=organization_id)
        except:
            pass

        return queryset


class OrganizationMemberRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = (OrganizationMemberPermission, )
    serializer_class = OrganizationMemberSerializer
    queryset = OrganizationMember.objects.all()
