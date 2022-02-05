from django.db import models


class Registry(models.Model):
    name = models.CharField(max_length=120, default='')
