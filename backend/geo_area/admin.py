from django.contrib import admin

from .models import GeoArea


# TODO to be deleted => test add action in admin menu
@admin.action(description="Ne rien faire")
def do_nothing(modeladmin, request, queryset):
    pass


class GeoAreaAdmin(admin.ModelAdmin):
    list_display = ("name",)
    list_filter = ("name",)
    # TODO to be deleted => test add action in admin menu
    actions = [do_nothing]


admin.site.register(GeoArea, GeoAreaAdmin)
