import os

from django.contrib.auth import get_user_model
from django.core.management import BaseCommand
from dotenv import load_dotenv

load_dotenv()


class Command(BaseCommand):
    help = "Создает админа в базе"

    def handle(self, *args, **options):
        get_user_model().objects.create_superuser(
            username=os.getenv("ADMIN_USERNAME"),
            email=os.getenv("ADMIN_EMAIL"),
            password=os.getenv("ADMIN_PASSWORD"),
        )

        self.stdout.write(self.style.SUCCESS("Админ создан"))
