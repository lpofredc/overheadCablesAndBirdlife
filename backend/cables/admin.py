from django.contrib import admin

from .models import Equipment, Observation, Pole, Segment

admin.site.register(Pole)
admin.site.register(Segment)
admin.site.register(Observation)
admin.site.register(Equipment)
