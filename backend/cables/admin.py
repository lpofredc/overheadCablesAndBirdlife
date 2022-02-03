from django.contrib import admin

from .models import Action, Infrastructure, Operation, Pole, Segment, Visit

admin.site.register(Infrastructure)
admin.site.register(Action)
admin.site.register(Pole)
admin.site.register(Segment)
admin.site.register(Visit)
admin.site.register(Operation)
