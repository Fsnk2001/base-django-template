from rest_framework.permissions import BasePermission


class IsAdminPermission(BasePermission):
    message = "Permission denied, you are not admin."

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_admin)
