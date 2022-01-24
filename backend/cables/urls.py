from django.urls import path

from .views import (  # EquipmentViewSet,; PoleEquipmentViewSet,; SegmentEquipmentViewSet,; SegmentViewSet,; VisitViewSet,
    PoleViewSet,
)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path(
        "poles/",
        PoleViewSet.as_view({"get": "list", "post": "create"}),
        name="pole_list",
    ),
    path(
        "poles/<int:pk>/",
        PoleViewSet.as_view(
            {
                "get": "retrieve",
                "put": "update",
                "patch": "partial_update",
                "delete": "destroy",
            }
        ),
        name="pole",
    ),
    # path("equipments/", EquipmentViewSet.as_view({"get": "list"})),
    # path(
    #     "equipments/<int:pk>",
    #     EquipmentViewSet.as_view({"get": "retrieve", "put": "update"}),
    # ),
    # path("pole-equipments/", PoleEquipmentViewSet.as_view({"get": "list"})),
    # path(
    #     "segment-equipments/", SegmentEquipmentViewSet.as_view({"get": "list"})
    # ),
    # path("equipmentsall/", WholeEquipmentViewSet.as_view({"get": "list"})),
    # re_path("equipments/(?P<pole>[0-9]+)/$", EquipmentViewSet.as_view({"get": "list"})),
    # re_path("^equipments/(?P<pole>[0-9]+)/$", EquipmentList.as_view()),
    # path("equipments/", EquipmentList.as_view()),
]
