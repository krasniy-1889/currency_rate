import os
from datetime import timedelta

from celery import Celery
from celery.schedules import crontab

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")

app = Celery("core")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()


@app.task
def debug_task():
    print("test")


app.conf.beat_schedule = {
    "update_currency_from_cbr": {
        "task": "apps.currency.tasks.update_currency_from_cbr",
        "schedule": crontab(minute="0", hour="12"),
    },
    "debug_task": {
        "task": "core.celery.debug_task",
        "schedule": timedelta(seconds=5),
    },
}
