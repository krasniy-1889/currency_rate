from core.celery import app

from .services import update_currency


@app.task
def update_currency_from_cbr():
    """Каждый день в 12 часов по москве проверяет обновления курса за последние 3 дня"""
    update_currency()
