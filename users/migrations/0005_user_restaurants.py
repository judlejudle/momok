# Generated by Django 4.1.1 on 2022-10-17 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("restaurants", "0004_remove_restaurant_restaurants"),
        ("users", "0004_alter_user_phone"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="restaurants",
            field=models.ManyToManyField(
                related_name="restaurant", to="restaurants.restaurant"
            ),
        ),
    ]
