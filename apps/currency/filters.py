import django_filters

from .models import Currency


class CurrencyFilter(django_filters.FilterSet):
    charcode = django_filters.CharFilter(field_name="charcode")
    date = django_filters.DateFilter(field_name="current_date")

    class Meta:
        model = Currency
        fields = ["charcode", "date"]
