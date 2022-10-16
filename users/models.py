from email.policy import default
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator


class User(AbstractUser):
    name = models.CharField(max_length=15, default="")
    email = models.CharField(max_length=50, default="")
    repetitive = models.BooleanField(default=True)
    spicyok = models.BooleanField(default=True)
    pricerange1 = models.IntegerField(
        default=8000,
        validators=[MinValueValidator(1000), MaxValueValidator(300000)],
    )
    pricerange2 = models.IntegerField(
        default=15000,
        validators=[MinValueValidator(pricerange1), MaxValueValidator(300000)],
    )
