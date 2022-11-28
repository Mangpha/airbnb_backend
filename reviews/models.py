from django.db import models
from django.core.validators import MaxValueValidator
from common.models import CommonModel
from experiences.models import Experience
from users.models import User
from rooms.models import Room

# Create your models here.


class Review(CommonModel):
    """
    Review Model Definition from a User to a Room or Experience
    """

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    room = models.ForeignKey(
        Room,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
    )
    experience = models.ForeignKey(
        Experience,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
    )
    payload = models.TextField()
    rating = models.PositiveIntegerField(
        validators=[MaxValueValidator(5)],
    )

    def __str__(self) -> str:
        return f"{self.user} / {self.rating}"
