from rest_framework import permissions
from rest_framework.exceptions import NotAuthenticated
from organizations.enums import OrganizationMemberTypes


SAFE_METHODS = ['GET']


class OrganizationDetailsPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True

        if not request.user.is_authenticated:
            raise NotAuthenticated()

        return obj.members.filter(member=request.user, role=OrganizationMemberTypes.ADMIN).exists()