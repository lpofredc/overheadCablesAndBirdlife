from django.contrib import admin

from .models import Species


class SpeciesAdmin(admin.ModelAdmin):
    list_display = ("code", "scientific_name", "vernacular_name", "active")
    list_filter = ("active",)
    ordering = ("scientific_name",)


admin.site.register(Species, SpeciesAdmin)
