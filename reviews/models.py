from django.db import models
from common.models import CommonModel


class Review(CommonModel):
    class ratingChoices(models.IntegerChoices):
        worst = 1
        bad = 2
        ok = 3
        good = 4
        excellent = 5

    rating = models.IntegerField(choices=ratingChoices.choices, null=False)
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="reviews",
    )
    restaurants = models.ForeignKey(
        "restaurants.Restaurant",
        on_delete=models.CASCADE,
        related_name="reviews",
    )
