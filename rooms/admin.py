from django.contrib import admin
from categories.models import Category

from rooms.models import Amenity, Room

# Register your models here.


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    """
    Room Admin Definition
    """

    list_display = (
        "name",
        "price",
        "kind",
        "total_amenities",
        "owner",
        "created_at",
    )
    list_filter = (
        "country",
        "city",
        "price",
        "rooms",
        "toilets",
        "pet_friendly",
        "kind",
        "amenities",
        "created_at",
        "updated_at",
    )

    def get_form(self, request, obj=None, **kwargs):
        form = super(RoomAdmin, self).get_form(request, obj, **kwargs)
        form.base_fields["category"].queryset = Category.objects.filter(kind="rooms")
        return form


@admin.register(Amenity)
class AmenityAdmin(admin.ModelAdmin):
    """
    Amenity Admin Definition
    """

    list_display = (
        "name",
        "description",
        "created_at",
        "updated_at",
    )
    readonly_fields = (
        "created_at",
        "updated_at",
    )
