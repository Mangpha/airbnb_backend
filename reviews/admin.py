from django.contrib import admin
from reviews.models import Review

# Register your models here.


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    """
    Review Admin Definition
    """

    list_display = (
        "__str__",
        "payload",
    )
    list_filter = ("rating",)