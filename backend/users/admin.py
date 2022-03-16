# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# Register your models here.
from .models import Organism, User


class OrganismAdmin(admin.ModelAdmin):
    list_display = ("id", "label", "short_label", "url", "email")


class UserAdmin(BaseUserAdmin):
    list_display = (
        "username",
        "organism",
        "email",
        "date_joined",
        "last_login",
        "is_staff",
        "is_superuser",
    )
    list_filter = [
        "organism",
    ]


admin.site.register(Organism, OrganismAdmin)
# admin.site.unregister(User)
admin.site.register(User, UserAdmin)
