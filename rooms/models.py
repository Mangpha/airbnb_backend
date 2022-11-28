from django.db import models
from categories.models import Category
from common.models import CommonModel
from users.models import User

# Create your models here.


class RoomKindChoices(models.TextChoices):
    ENTIRE_PLACE = ("entire_place", "Entire Place")
    PRIVATE_ROOM = ("private_room", "Private Room")
    SHARED_ROOM = ("shared_room", "Shared Room")


class Amenity(CommonModel):
    """
    Amenity Model Definition
    """

    name = models.CharField(
        max_length=150,
    )
    description = models.CharField(
        max_length=150,
        null=True,
        blank=True,
    )

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name_plural = "Amenities"


class Room(CommonModel):
    """
    Room Model Definition
    """

    name = models.CharField(
        max_length=180,
        default="",
    )
    country = models.CharField(
        max_length=50,
        default="South Korea",
    )
    city = models.CharField(
        max_length=80,
        default="Seoul",
    )
    price = models.PositiveIntegerField()
    rooms = models.PositiveIntegerField()
    toilets = models.PositiveIntegerField()
    description = models.TextField()
    address = models.CharField(
        max_length=250,
    )
    pet_friendly = models.BooleanField(
        default=True,
    )
    kind = models.CharField(
        max_length=20,
        choices=RoomKindChoices.choices,
    )
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    amenities = models.ManyToManyField(Amenity)
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    def __str__(self) -> str:
        return self.name
