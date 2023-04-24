from django.conf import settings
from django.contrib.gis.admin import GISModelAdmin

# from django.contrib import admin

# Register your models here.


# Register your models here.
class GisModelAdmin(GISModelAdmin):
    gis_widget_kwargs = {
        "attrs": {
            "default_lat": settings.DEFAULT_LAT,
            "default_lon": settings.DEFAULT_LON,
        }
    }
