from rest_framework import permissions


class OwnerOrReadOmly(permissions.IsAuthenticatedOrReadOnly):
    """Только автор может изменять посты и комментарии."""

    def has_object_permission(self, request, view, obj):
        return (
            obj.author == request.user
            or request.method in permissions.SAFE_METHODS
        )
