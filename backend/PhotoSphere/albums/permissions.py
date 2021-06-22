from rest_framework import permissions
from rest_framework.exceptions import NotAuthenticated


SAFE_METHODS = ['GET']


class AlbumDetailsPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True

        if not request.user.is_authenticated:
            raise NotAuthenticated()
        return obj.owner.user.id == request.user.id
