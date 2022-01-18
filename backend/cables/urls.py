from django.urls import include, path
from rest_framework import routers

from .views import EquipmentViewSet, PoleViewSet, SegmentViewSet, VisitViewSet

router = routers.SimpleRouter()
router.register(r"segments", SegmentViewSet)
router.register(r"visits", VisitViewSet)
router.register(r"equipments", EquipmentViewSet)
urlpatterns = router.urls

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path("", include(router.urls)),
    path(
        "poles/",
        PoleViewSet.as_view({"get": "list"}),
        name="pole_list",
    ),
    path(
        "poles/<int:pk>/",
        PoleViewSet.as_view({"get": "retrieve"}),
        name="pole",
    ),
]
