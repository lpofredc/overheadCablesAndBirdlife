from django.urls import include, path
from rest_framework import routers

app_name = "cables"

from .views import (
    EquipmentViewSet,
    ObservationViewSet,
    PoleViewSet,
    SegmentViewSet,
)

router = routers.SimpleRouter()
router.register(r"poles", PoleViewSet)
router.register(r"segments", SegmentViewSet)
router.register(r"observations", ObservationViewSet)
router.register(r"equipments", EquipmentViewSet)
urlpatterns = router.urls

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path("", include(router.urls)),
]
