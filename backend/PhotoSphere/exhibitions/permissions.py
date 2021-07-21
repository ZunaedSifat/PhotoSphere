from rest_framework.permissions import BasePermission
from rest_framework.exceptions import NotAuthenticated
from organizations.enums import OrganizationMemberTypes


SAFE_METHODS = ['GET']


class ExhibitionPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True

        if not request.user.is_authenticated:
            raise NotAuthenticated()

        return obj.organizer.members.filter(
            member=request.user, role__in=[OrganizationMemberTypes.ADMIN, OrganizationMemberTypes.EDITOR]
        ).exists()


class ExhibitionEntryPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True

        if not request.user.is_authenticated:
            raise NotAuthenticated()

        return obj.exhibition.organizer.members.filter(
            member=request.user, role__in=[OrganizationMemberTypes.ADMIN, OrganizationMemberTypes.EDITOR]
        ).exists()