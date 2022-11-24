from django.db import models
from django.contrib.auth.models import AbstractUser


class GenderChoices(models.TextChoices):
    """
    Gender Choices Class
    """

    MALE = ("male", "Male")
    FEMALE = ("female", "Female")


class LanguageChoices(models.TextChoices):
    """
    Language Choices Class
    """

    KR = ("kr", "Korean")
    EN = ("en", "English")


class CurrencyChoices(models.TextChoices):
    """
    Currency Choices Class
    """

    WON = ("won", "Won")
    USD = ("usd", "Dollar")


# Create your models here.
class User(AbstractUser):
    """
    User Model Definition
    """

    first_name = models.CharField(
        max_length=150,
        editable=False,
    )
    last_name = models.CharField(
        max_length=150,
        editable=False,
    )
    name = models.CharField(
        max_length=150,
        default="",
    )
    avatar = models.ImageField(
        blank=True,
    )
    gender = models.CharField(
        max_length=10,
        choices=GenderChoices.choices,
    )
    is_host = models.BooleanField(
        default=False,
    )
    language = models.CharField(
        max_length=3,
        choices=LanguageChoices.choices,
    )
    currency = models.CharField(
        max_length=5,
        choices=CurrencyChoices.choices,
    )
