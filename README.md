# api_final

# Описание
Проект представляет собой API для социальной сети Yatube. 
Пользователи могут публиковать посты, комментировать их и подписываться на авторов.

# Технологии
Python 3.12
Django 5.1.1
Django REST Framework
JWT (Simple JWT)
Djoser

# Как запустить проект:

1. Клонировать репозиторий.
2. Установить зависимости: `pip install -r requirements.txt`.
3. Выполнить миграции: `python manage.py migrate`.
4. Запустить сервер: `python manage.py runserver`.

# Примеры запросов к API:

GET /api/v1/posts/ — получить список всех постов.

POST /api/v1/jwt/create/ — получение JWT-токена.

GET /api/v1/follow/ — получение подписок текущего пользователя.