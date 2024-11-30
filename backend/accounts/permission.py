from rest_framework.permissions import BasePermission

class IsStaffUser(BasePermission):
    # Allows access only to users with is_staff set to True.
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and request.user.is_staff
