# django_user_online

Функция для django, чтобы смотреть кто из пользователей онлайн. Сохраняется в кэш.

Добавляем настройки в settings.py

```python
MIDDLEWARE_CLASSES = (
    'main.middleware.ActiveUserMiddleware',
)
```

```python
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': '/var/tmp/django_cache',
        'TIMEOUT': 300,
    }
}


# Number of seconds that we will keep track of inactive users for before
# their last seen is removed from the cache
USER_LASTSEEN_TIMEOUT = 60 * 60 * 24 * 7
```

Я выбрал файловый кэш, потому что у меня стоит SSD. Можете подробно почитать в документации про кэш. 
