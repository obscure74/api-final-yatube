"""Настройка административной панели приложения Posts."""
from django.contrib import admin

from .models import Comment, Follow, Group, Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """Настройка отображения модели Post."""

    list_display = ('pk', 'text', 'pub_date', 'author', 'group')
    search_fields = ('text',)
    list_filter = ('pub_date',)
    empty_value_display = '-пусто-'


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    """Настройка отображения модели Group."""

    list_display = ('title', 'slug', 'description')
    search_fields = ('title',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """Настройка отображения модели Comment."""

    list_display = ('pk', 'post', 'author', 'text', 'created')
    search_fields = ('text',)


@admin.register(Follow)
class FollowAdmin(admin.ModelAdmin):
    """Настройка отображения модели Follow."""

    list_display = ('user', 'following')
