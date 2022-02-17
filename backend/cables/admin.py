from django.contrib import admin

from commons.admin import GisModelAdmin

from .models import Diagnosis, Line, Operation, Point

admin.site.register(Point, GisModelAdmin)
admin.site.register(Line, GisModelAdmin)
admin.site.register(Diagnosis)
admin.site.register(Operation)
