from unittest.util import _MAX_LENGTH
from django.db import models
from common.models import CommonModel


class Restaurant(CommonModel):
    class TypeChoices(models.TextChoices):
        chinese = ("chinese", "Chinese")
        korean = ("korean", "Korean")
        japanese = ("japanese", "Japanese")
        fushion = ("fushion", "Fushion")
        other = ("other", "Other")

    name = models.TextField(max_length=30)
    type = models.CharField(
        max_length=30,
        choices=TypeChoices.choices,
    )
    spicy = models.BooleanField(default=False)
