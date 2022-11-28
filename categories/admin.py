from django.contrib import admin

from categories.models import Category
from rooms.admin import RoomAdmin

# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """
    Category Admin Definition
    """

    list_display = (
        "name",
        "kind",
    )
    list_filter = ("kind",)
