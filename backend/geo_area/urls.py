from django.urls import include, path
from rest_framework import routers

from .views import GeoAreaViewSet

app_name = "geo_area"

router = routers.SimpleRouter()
router.register(r"areas", GeoAreaViewSet)
urlpatterns = router.urls

urlpatterns = [
    path("", include(router.urls)),
]
