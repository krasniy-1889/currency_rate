from django.urls import path

from .views import CurrencyByValute

app_name = "currency"

urlpatterns = [
    path("", CurrencyByValute.as_view(), name="valute"),
]
