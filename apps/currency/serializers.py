from rest_framework import serializers

from .models import Currency


class CurrencySerializer(serializers.ModelSerializer):
    date = serializers.DateField(source="current_date")

    class Meta:
        model = Currency
        fields = ["charcode", "rate", "date"]
