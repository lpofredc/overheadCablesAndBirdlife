from django.contrib import admin

from commons.admin import GisModelAdmin

from .models import GeoArea


class GeoAreaAdmin(GisModelAdmin):
    list_display = (
        "type",
        "code",
        "name",
    )
    list_filter = ("type",)


admin.site.register(GeoArea, GeoAreaAdmin)
