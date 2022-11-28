from django.contrib import admin
from categories.models import Category
from experiences.models import Experience, Perk

# Register your models here.


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    """
    Experience Admin Definition
    """

    list_display = (
        "name",
        "price",
        "start",
        "end",
        "created_at",
    )
    list_filter = ("category",)

    def get_form(self, request, obj=None, **kwargs):
        form = super(ExperienceAdmin, self).get_form(request, obj, **kwargs)
        form.base_fields["category"].queryset = Category.objects.filter(
            kind="experiences"
        )
        return form


@admin.register(Perk)
class PerkAdmin(admin.ModelAdmin):
    """
    Perk Admin Definition
    """

    list_display = (
        "name",
        "details",
        "explanation",
    )
