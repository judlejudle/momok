from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    name = models.CharField(max_length=15, default="")
    email = models.CharField(max_length=50, default="")
    repetitive = models.BooleanField(default=True)
