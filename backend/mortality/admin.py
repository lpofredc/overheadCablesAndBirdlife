from django.conf import settings
from django.contrib import admin

from commons.admin import GisModelAdmin

from .models import Mortality

admin.site.register(Mortality, GisModelAdmin)
