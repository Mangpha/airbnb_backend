from django.db import models
from common.models import CommonModel
from rooms.models import Room
from experiences.models import Experience

# Create your models here.


class Photo(CommonModel):
    """
    Photo Model Definition
    """

    file = models.ImageField()
    description = models.CharField(
        max_length=140,
    )
    room = models.ForeignKey(
        Room,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    experience = models.ForeignKey(
        Experience,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )

    def __str__(self) -> str:
        return "Photo file"


class Video(CommonModel):
    """
    Video Model Definition
    """

    file = models.FileField()
    experience = models.OneToOneField(
        Experience,
        on_delete=models.CASCADE,
    )

    def __str__(self) -> str:
        return "Video File"
