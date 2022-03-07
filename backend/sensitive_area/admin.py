from django.contrib import admin

from commons.admin import GisModelAdmin

from .models import SensitiveArea

admin.site.register(SensitiveArea, GisModelAdmin)
