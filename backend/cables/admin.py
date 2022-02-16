from django.contrib import admin

from commons.admin import GisModelAdmin

from .models import Operation, Pole, Segment, Visit

admin.site.register(Pole, GisModelAdmin)
admin.site.register(Segment, GisModelAdmin)
admin.site.register(Visit)
admin.site.register(Operation)
