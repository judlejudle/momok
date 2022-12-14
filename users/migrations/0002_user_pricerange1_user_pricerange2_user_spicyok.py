# Generated by Django 4.1.1 on 2022-10-16 21:53

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="pricerange1",
            field=models.IntegerField(
                default=8000,
                validators=[
                    django.core.validators.MinValueValidator(1000),
                    django.core.validators.MaxValueValidator(300000),
                ],
            ),
        ),
        migrations.AddField(
            model_name="user",
            name="pricerange2",
            field=models.IntegerField(
                default=15000,
                validators=[
                    django.core.validators.MinValueValidator(
                        models.IntegerField(
                            default=8000,
                            validators=[
                                django.core.validators.MinValueValidator(1000),
                                django.core.validators.MaxValueValidator(300000),
                            ],
                        )
                    ),
                    django.core.validators.MaxValueValidator(300000),
                ],
            ),
        ),
        migrations.AddField(
            model_name="user",
            name="spicyok",
            field=models.BooleanField(default=True),
        ),
    ]
