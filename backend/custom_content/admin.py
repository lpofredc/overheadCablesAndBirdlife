from django.contrib import admin
from django.utils.html import mark_safe

from .models import News, Partners

# Register your models here.


class PartnersAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "short_name",
        "url",
        "logo",
        "logo_image",
    )

    readonly_fields = ["logo_image"]

    def logo_image(self, obj):
        return mark_safe(
            '<img src="{url}" width="{width}" height={height} />'.format(
                url=obj.logo.url,
                width=obj.logo.width,
                height=obj.logo.height,
            )
        )


class NewsAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "intro",
        "private",
        "timestamp_create",
        "created_by",
    )
    list_filter = ("created_by",)

    def save_model(self, request, obj, form, change):
        if obj.id is None:
            obj.created_by = request.user
            obj.updated_by = request.user
            super().save_model(request, obj, form, change)
        else:
            obj.updated_by = request.user
            super().save_model(request, obj, form, change)


admin.site.register(Partners, PartnersAdmin)
admin.site.register(News, NewsAdmin)
