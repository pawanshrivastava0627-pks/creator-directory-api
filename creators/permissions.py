from rest_framework.permissions import BasePermission


class IsOwnerOrAdmin(BasePermission):

    def has_permission(self, request, view):

        # Read-only sabke liye
        if request.method in ["GET", "HEAD", "OPTIONS"]:
            return True

        # Write sirf owner/admin
        return request.user.role in ["owner", "admin"]