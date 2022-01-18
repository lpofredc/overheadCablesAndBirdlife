from django.urls import include, path
from rest_framework import routers

from .views import GeoAreaGeoViewSet, GeoAreaViewSet

app_name = "geo_area"

router = routers.SimpleRouter()
router.register(r"areas", GeoAreaGeoViewSet)
router.register(r"areas_no_geom", GeoAreaViewSet)
urlpatterns = router.urls

urlpatterns = [
    path("", include(router.urls)),
]
