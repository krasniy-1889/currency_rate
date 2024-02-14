from datetime import datetime, timedelta

import httpx
from django.core.management import BaseCommand
from dotenv import load_dotenv

from apps.currency.models import Currency
from apps.currency.services import update_currency

load_dotenv()


class Command(BaseCommand):
    help = "Заполняет баззу тестовыми данным"

    def handle(self, *args, **options):
        self.stdout.write(self.style.NOTICE("Начинаем заполнять базу данных"))
        update_currency(30)
        self.stdout.write(self.style.SUCCESS("База заполнена"))
