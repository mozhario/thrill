from rest_framework import permissions


class IsMeOrReadOnly(permissions.BasePermission):
    """
    Only allows user to edit his own account
    """
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj == request.user


class IsPostAuthorOrReadOnly(permissions.BasePermission):
    """
    Only author of the post can edit the post
    """
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user == request.user


class IsCommunityAdminOrReadOnly(permissions.BasePermission):
    """
    Only author of the post can edit the post
    """
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.community.admin == request.user