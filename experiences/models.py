from django.db import models
from common.models import CommonModel
from users.models import User

# Create your models here.


class Perk(CommonModel):
    """
    Perk Model Definition

    (What is included on an Experience)
    """

    name = models.CharField(
        max_length=100,
    )
    details = models.CharField(
        max_length=250,
        blank=True,
        default="",
    )
    explanation = models.TextField(
        blank=True,
        default="",
    )

    def __str__(self) -> str:
        return self.name


class Experience(CommonModel):
    """
    Experience Model Definition
    """

    country = models.CharField(
        max_length=50,
        default="South Korea",
    )
    city = models.CharField(
        max_length=80,
        default="Seoul",
    )
    name = models.CharField(
        max_length=250,
    )
    host = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    price = models.PositiveIntegerField()
    address = models.CharField(
        max_length=250,
    )
    start = models.TimeField()
    end = models.TimeField()
    description = models.TextField()
    perks = models.ManyToManyField(Perk)

    def __str__(self) -> str:
        return self.name
