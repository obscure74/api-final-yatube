"""Модуль описания прав доступа для API."""
from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    """Разрешает чтение всем, а редактирование только автору."""

    def has_object_permission(self, request, view, obj):
        """Проверяет наличие прав у пользователя на действие с объектом."""
        return (
            request.method in permissions.SAFE_METHODS
            or obj.author == request.user
        )
