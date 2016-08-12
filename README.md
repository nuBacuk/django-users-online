# django_user_online

Функция для django, чтобы смотреть кто из пользователей онлайн. Сохраняется в кэш.

Добавляем настройки в **settings.py**

**Указываем путь к middleware(промежуточный слой).**
```python
MIDDLEWARE_CLASSES = (
    'main.middleware.ActiveUserMiddleware',
)
```

**Я выбрал файловый кэш, потому что у меня стоит SSD. Можете подробно почитать в документации про кэш.**
Выбрал место для хранения кэша, и время сколько будет хранится кэш **300 секунд**
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

Добавляем в **url.py**
```python
from main.view import usersonline

urlpatterns = patterns('',
    url(r'^$', 'views.home', name='Главная'),
	url(r'^online/$', usersonline),
```

<img src="https://habrastorage.org/files/280/391/f2a/280391f2ab2c481c86ca35b1fc78e263.png"/>
