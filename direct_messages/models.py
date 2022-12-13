from django.db import models
from common.models import CommonModel
from users.models import User

# Create your models here.


class ChatRoom(CommonModel):
    """
    Chat Room Model Definition
    """

    users = models.ManyToManyField(
        User,
    )

    def __str__(self) -> str:
        return "Chat Room"


class ChatMessage(CommonModel):
    """
    Chat Message Model Definition
    """

    text = models.TextField()
    user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    room = models.ForeignKey(
        ChatRoom,
        on_delete=models.CASCADE,
    )

    def __str__(self) -> str:
        return f"{self.user} : {self.text}"
