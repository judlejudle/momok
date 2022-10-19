from django.db import models
from common.models import CommonModel


class Restaurant(CommonModel):
    class TypeChoices(models.TextChoices):
        chinese = ("chinese", "Chinese")
        korean = ("korean", "Korean")
        japanese = ("japanese", "Japanese")
        fushion = ("fushion", "Fushion")
        other = ("other", "Other")

    class SpicyChoices(models.IntegerChoices):
        baby = 1
        human = 2
        pepper = 3

    name = models.TextField(max_length=30)
    type = models.CharField(
        max_length=30,
        choices=TypeChoices.choices,
    )
    spicy = models.IntegerField(
        choices=SpicyChoices.choices,
    )
    best = models.CharField(max_length=30)
    address = models.CharField(max_length=130)

    def rating(restaurants):
        count = restaurants.reviews.count()
        if count == 0:
            return "No Review"
        else:
            total_rating = 0
            for review in restaurants.reviews.all().values("rating"):
                total_rating += review["rating"]
                return round(total_rating / count, 2)

    def __str__(self) -> str:
        return self.name
