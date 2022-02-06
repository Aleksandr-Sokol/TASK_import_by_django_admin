from django.db import models
from django.db.models import ForeignKey, PROTECT


class Zmk(models.Model):
    name = models.CharField(max_length=120, null=False)

    class Meta:
        verbose_name_plural = "Zmk"


class Registry(models.Model):
    num = models.PositiveIntegerField()
    name = models.CharField(max_length=120, default='')
    weight = models.FloatField()
    departure_date = models.DateField(null=True, blank=True)
    receiving_date = models.DateField(null=True, blank=True)
    zmk = ForeignKey(Zmk,
                     related_name='rts',
                     on_delete=PROTECT,
                     null=True,
                     )

    class Meta:
        verbose_name_plural = "RTS"
