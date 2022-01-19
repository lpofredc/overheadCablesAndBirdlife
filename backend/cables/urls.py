from django.urls import include, path
from rest_framework import routers

from .views import (
    EquipmentViewSet,
    PoleEquipmentViewSet,
    SegmentEquipmentViewSet,
    SegmentViewSet,
    VisitViewSet,
)

router = routers.SimpleRouter()
router.register(r"segments", SegmentViewSet)
router.register(r"visits", VisitViewSet)
# router.register(r"equipments", EquipmentViewSet)
urlpatterns = router.urls

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path("", include(router.urls)),
    # path(
    #     "poles/",
    #     PoleViewSet.as_view({"get": "list"}),
    #     name="pole_list",
    # ),
    # path(
    #     "poles/<int:pk>/",
    #     PoleViewSet.as_view({"get": "retrieve"}),
    #     name="pole",
    # ),
    path("equipments/", EquipmentViewSet.as_view({"get": "list"})),
    path("pole-equipments/", PoleEquipmentViewSet.as_view({"get": "list"})),
    path(
        "segment-equipments/", SegmentEquipmentViewSet.as_view({"get": "list"})
    ),
    # path("equipmentsall/", WholeEquipmentViewSet.as_view({"get": "list"})),
    # re_path("equipments/(?P<pole>[0-9]+)/$", EquipmentViewSet.as_view({"get": "list"})),
    # re_path("^equipments/(?P<pole>[0-9]+)/$", EquipmentList.as_view()),
    # path("equipments/", EquipmentList.as_view()),
]
