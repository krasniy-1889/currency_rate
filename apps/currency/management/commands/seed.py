from datetime import datetime, timedelta

import httpx
from django.core.management import BaseCommand
from dotenv import load_dotenv

from apps.currency.models import Currency

load_dotenv()


class Command(BaseCommand):
    help = "Заполняет баззу тестовыми данным"

    def handle(self, *args, **options):
        current_date = datetime.now()
        self.stdout.write(self.style.NOTICE("Начинаем заполнять базу данных"))

        for _ in range(30):
            current_date = current_date - timedelta(days=1)
            date_str = current_date.strftime("%Y/%m/%d")
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

        self.stdout.write(self.style.SUCCESS("База заполнена"))
