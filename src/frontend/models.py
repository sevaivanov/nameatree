from django.db import models
from datetime import date

class Tree(models.Model):

    name = models.CharField(
        max_length = 20,
        blank = False
    )

    latitude = models.DecimalField(
        max_digits = 11,
        decimal_places = 8
    )

    longitude = models.DecimalField(
        max_digits = 11,
        decimal_places = 8
    )

    memory = models.DateField(
        max_length = 1000,
        blank = False
    )

    shared_date = models.DateField(
        default = date.today,
        blank = False
    )
