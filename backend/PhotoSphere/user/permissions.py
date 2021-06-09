from rest_framework import permissions
from rest_framework.exceptions import NotAuthenticated


SAFE_METHODS = ['GET']


class ProfileListCreatePermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET' and not request.user.is_authenticated:
            raise NotAuthenticated()
        return True
