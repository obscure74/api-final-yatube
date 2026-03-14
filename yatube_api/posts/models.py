"""Модели для приложения Posts в проекте Yatube API."""
from django.contrib.auth import get_user_model
from django.db import models

from posts.constants import LIMIT_TEXT_STR

User = get_user_model()


class Group(models.Model):
    """Модель для групп."""

    title = models.CharField('Заголовок', max_length=200)
    slug = models.SlugField('Идентификатор', unique=True)
    description = models.TextField('Описание')

    def __str__(self):
        """Возвращает строковое представление группы."""
        return self.title


class Post(models.Model):
    """Модель для публикаций."""

    text = models.TextField()
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Автор'
    )
    image = models.ImageField(
        'Изображение',
        upload_to='posts/',
        null=True,
        blank=True
    )
    group = models.ForeignKey(
        Group,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name='Группа'
    )

    class Meta:
        """Мета-данные модели поста."""

        ordering = ('pub_date',)
        default_related_name = 'posts'

    def __str__(self):
        """Возвращает укороченный текст поста."""
        return self.text[:LIMIT_TEXT_STR]


class Comment(models.Model):
    """Модель для комментариев к публикациям."""

    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Автор'
    )
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        verbose_name='Пост'
    )
    text = models.TextField('Текст комментария')
    created = models.DateTimeField(
        'Дата добавления',
        auto_now_add=True,
        db_index=True
    )

    class Meta:
        """Мета-данные модели комментария."""

        default_related_name = 'comments'

    def __str__(self):
        """Возвращает информацию о комментарии."""
        return f'Комментарий {self.author} к посту {self.post}'


class Follow(models.Model):
    """Модель для подписок на авторов."""

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='follower',
    )
    following = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='following',
    )

    class Meta:
        """Мета-данные модели подписок."""

        constraints = [
            models.UniqueConstraint(
                fields=['user', 'following'],
                name='unique_follow'
            )
        ]

    def __str__(self):
        """Возвращает информацию о подписке."""
        return f'{self.user} подписан на {self.following}'
