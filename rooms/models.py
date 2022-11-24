from django.db import models
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
    )


class Room(CommonModel):
    """
    Room Model Definition
    """

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
