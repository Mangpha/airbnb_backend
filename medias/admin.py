from django.contrib import admin
from medias.models import Photo, Video

# Register your models here.


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    """
    Photo Admin Definition
    """

    pass


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    """
    Video Admin Definition
    """

    pass
