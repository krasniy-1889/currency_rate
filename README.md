# Инструкция

1. Запускаете докер командой:

```docker compose up ```

2. Поднимаете контейнер, в результате поднимутся Redis, Celery и Beat.

3. Заполните базу данных, выполните команду:

```docker compose exec web poetry run python3 manage.py admin ```

Это создаст администратора.
Данные для входа:
- Логин: admin
- Пароль: admin

1. Заполните базу валютами за последние 30 дней командой:
```docker compose exec web poetry run python3 manage.py seed ```

Переходим на http://127.0.0.1:8000
