from django.db import models


class Currency(models.Model):
    charcode = models.CharField(max_length=5)
    rate = models.FloatField()
    current_date = models.DateField(db_index=True)

    def __str__(self):
        return f"{self.charcode} - {self.rate} - {self.current_date}"
