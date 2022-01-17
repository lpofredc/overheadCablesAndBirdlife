from django.contrib import admin

from .models import Equipment, Pole, Segment, Visit

admin.site.register(Pole)
admin.site.register(Segment)
admin.site.register(Visit)
admin.site.register(Equipment)
