from rest_framework import permissions


class ActiveUsers(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_active:
            return True
        return False
