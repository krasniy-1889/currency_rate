from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager


class CustomUser(AbstractUser):
    objects = CustomUserManager()

    def __str__(self):
        return self.username

    class Meta:
        db_table = "user_users"
        verbose_name = "User"
        verbose_name_plural = "Users"
