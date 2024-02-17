# blog/permissions.py
from rest_framework import permissions


class IsEditorOrAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_staff or (
            request.user == obj.author and
            view.action in ['update', 'partial_update', 'destroy']
        ):
            return True
        return False
