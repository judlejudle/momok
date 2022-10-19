from django.contrib import admin
from .models import Restaurant


@admin.register(Restaurant)
class Restaurant(admin.ModelAdmin):
    list_display = (
        "name",
        "type",
        "spicy",
        "rating",
    )
