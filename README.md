# API для социальной сети Yatube

### Описание
REST API для платформы Yatube. Проект позволяет взаимодействовать с постами, комментариями, сообществами и системой подписок через стандартные HTTP-запросы. Поддерживает аутентификацию с помощью JWT-токенов и предоставляет документацию в формате Redoc.

### Технологический стек
* **Python** 3.12
* **Django** 5.1
* **Django Rest Framework** (DRF)
* **Simple JWT** (Аутентификация)
* **Djoser** (Управление пользователями)
* **Pytest** (Тестирование)

---

### Как запустить проект:

1. Клонировать репозиторий и перейти в него в командной строке:
```bash
git clone [https://github.com/obscure74/api_final_yatube.git](https://github.com/obscure74/api_final_yatube.git)
cd api_final_yatube

```
Cоздать и активировать виртуальное окружение:
```bash
python -m venv venv
source venv/Scripts/activate  # Для Windows: venv/Scripts/activate

```
Установить зависимости из файла requirements.txt:
```bash
pip install -r requirements.txt

```
Выполнить миграции:
```bash
python manage.py migrate

```
Запустить проект:
```bash
python manage.py runserver

```
### Примеры запросов к API

1. Получение JWT-токена

POST /api/v1/jwt/create/

Тело запроса:
```JSON
{
    "username": "your_username",
    "password": "your_password"
}
```
Ответ:
```JSON
{
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbG...",
    "access": "eyJ0eXAiOiJKV1QiLCJhbG..."
}
```
2. Получение списка постов (пагинация включена)

GET /api/v1/posts/?limit=2&offset=0

Ответ:
```JSON
{
    "count": 100,
    "next": "[http://127.0.0.1:8000/api/v1/posts/?limit=2&offset=2](http://127.0.0.1:8000/api/v1/posts/?limit=2&offset=2)",
    "previous": null,
    "results": [
        {
            "id": 1,
            "author": "user1",
            "text": "Текст первого поста",
            "pub_date": "2026-03-14T12:00:00Z",
            "image": null,
            "group": 1
        },
        {
            "id": 2,
            "author": "user1",
            "text": "Текст второго поста",
            "pub_date": "2026-03-14T12:05:00Z",
            "image": null,
            "group": null
        }
    ]
}
```
3. Подписка на автора

POST /api/v1/follow/

Тело запроса:
```JSON
{
    "following": "author_username"
}
```
