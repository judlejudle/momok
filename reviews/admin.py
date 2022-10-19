from django.contrib import admin
from .models import Review


@admin.register(Review)
class reviewAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "restaurants",
        "rating",
    )
