# django_user_online

<img src="https://habrastorage.org/files/e76/a99/fd2/e76a99fd274e4b5dbba2783e077bfa64.png"/>
Модуль для просмотра пользователей онлайн.

1. Добавить django-users-online приложение в установленные приложения::
```python
    INSTALLED_APPS = (
        ...
        'django-users-online',
    )
```
2. Подключить приложение в urls::
```python
    url(r'^online/', include('django-users-online.urls')),
```
3. Добавить в settings.py настройки для кэша, и другие параметры::
```python
    CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': '/var/tmp/django_cache',
        'TIMEOUT': 90000,
    }
}

    # Время в секундах после которого пользователь не онлайн
    USER_TIMEOUT = 900
    # Number of seconds that we will keep track of inactive users for before
    # their last seen is removed from the cache
    USER_LASTSEEN_TIMEOUT = 60 * 60 * 24 * 7
```
4. В приложении указана стандартная модель пользователя, если у вас свою нужно изменить::
```python
    from django.contrib.auth.models import User
```

5. Добавить в папку с шаблонами online.html::
```html
    {% block content %}
        <table border="1">
        <tr>
                <th scope="row">#</th>
                <td>Фамилия</td>
                <td>Логин</td>
                <td>IP</td>
              </tr>
        {% for item in online %}
              <tr>
                <th scope="row">{{ item.0 }}</th>
                <td>{{ item.1 }}</td>
                <td>{{ item.2 }}</td>
                <td>{{ item.3 }}</td>
              </tr>
        {% endfor %}
        </table>
    {% endblock %}
```
5. Переходим по адресу http://127.0.0.1/online
