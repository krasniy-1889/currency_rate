from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListAPIView

from .filters import CurrencyFilter
from .models import Currency
from .serializers import CurrencySerializer
from .tasks import update_currency_from_cbr


class CurrencyByValute(ListAPIView):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = CurrencyFilter
