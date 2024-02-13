from datetime import datetime, timedelta

import httpx

from .models import Currency


def update_currency():
    """Проверяет обновления курса за последние 3 дня"""
    current_date = datetime.now()
    for _ in range(6):
        current_date = current_date - timedelta(days=1)
        date_str = current_date.strftime("%Y/%m/%d")
        currency_date_exists = Currency.objects.filter(
            current_date=current_date.date()
        ).exists()
        if currency_date_exists:
            continue

        res = httpx.get(
            f"https://www.cbr-xml-daily.ru/archive/{date_str}/daily_json.js"
        )

        if res.status_code != 200:
            continue

        valutes = []

        data = res.json()["Valute"]

        for valute in data:
            valutes.append(
                Currency(
                    charcode=valute,
                    rate=data[valute]["Value"],
                    current_date=current_date.date(),
                )
            )

        Currency.objects.bulk_create(valutes)
