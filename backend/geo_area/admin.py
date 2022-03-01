from django.contrib import admin

from commons.admin import GisModelAdmin

from .models import GeoArea


class GeoAreaAdmin(GisModelAdmin):
    list_display = ("name",)
    list_filter = ("name",)


admin.site.register(GeoArea, GeoAreaAdmin)
