from django.db import models
from common.models import CommonModel
from experiences.models import Experience
from rooms.models import Room
from users.models import User

# Create your models here.


class Wishlist(CommonModel):
    """
    Wishlist Model Definition
    """

    name = models.CharField(max_length=150)
    rooms = models.ManyToManyField(
        Room,
    )
    experiences = models.ManyToManyField(
        Experience,
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )

    def __str__(self) -> str:
        return self.name
