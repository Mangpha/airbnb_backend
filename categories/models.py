from django.db import models

from common.models import CommonModel

# Create your models here.


class CategoryKindChoices(models.TextChoices):
    ROOM = "rooms", "Rooms"
    EXPERIENCE = "experiences", "Experiences"


class Category(CommonModel):
    """
    Room or Experience Category Model Definition
    """

    name = models.CharField(max_length=50)
    kind = models.CharField(
        max_length=20,
        choices=CategoryKindChoices.choices,
    )

    def __str__(self) -> str:
        return f"{self.kind.title()}: {self.name}"

    class Meta:
        verbose_name_plural = "Categories"
