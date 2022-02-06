from django.db import models
from django.db.models import ForeignKey, CASCADE


class ExcelFile(models.Model):
    file = models.FileField()
    date_import = models.DateTimeField(auto_now_add=True)


class Zmk(models.Model):
    name = models.CharField(max_length=120, null=False)

    class Meta:
        verbose_name_plural = "Zmk"


class Object(models.Model):
    name = models.CharField(max_length=120, default='')
    zmk = ForeignKey(Zmk,
                     related_name='object',
                     on_delete=CASCADE,
                     null=True,
                     )

    class Meta:
        verbose_name_plural = "Object"


class Registry(models.Model):
    num = models.PositiveIntegerField(default=0)
    weight = models.FloatField(default=0.0)
    departure_date = models.DateField(null=True, blank=True)
    receiving_date = models.DateField(null=True, blank=True)
    object = ForeignKey(Object,
                        related_name='rts',
                        on_delete=CASCADE,
                        null=True,
                        )
    zmk = ForeignKey(Zmk,
                     related_name='rts',
                     on_delete=CASCADE,
                     null=True,
                     )

    class Meta:
        verbose_name_plural = "RTS"
