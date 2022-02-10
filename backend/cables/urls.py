from django.urls import path

from .views import (
    ActionViewSet,
    InfrastructureViewSet,
    OperationViewSet,
    PoleViewSet,
    SegmentViewSet,
    VisitViewSet,
)

urlpatterns = [
    # No create, update or delete on Infrastructure parent class: to be done on inherited classes
    path(
        "infrastructures/",
        InfrastructureViewSet.as_view({"get": "list"}),
        name="infrastructure_list",
    ),
    path(
        "infrastructures/<int:pk>/",
        InfrastructureViewSet.as_view({"get": "retrieve"}),
        name="infrastructure_detail",
    ),
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
        name="pole_detail",
    ),
    path(
        "segments/",
        SegmentViewSet.as_view({"get": "list", "post": "create"}),
        name="segment_list",
    ),
    path(
        "segments/<int:pk>/",
        SegmentViewSet.as_view(
            {
                "get": "retrieve",
                "put": "update",
                "patch": "partial_update",
                "delete": "destroy",
            }
        ),
        name="segment_detail",
    ),
    # No create, update or delete on Infrastructure parent class: to be done on inherited classes
    path(
        "actions/",
        ActionViewSet.as_view({"get": "list"}),
        name="action_list",
    ),
    path(
        "actions/<int:pk>/",
        ActionViewSet.as_view({"get": "retrieve"}),
        name="action_detail",
    ),
    path(
        "visits/",
        VisitViewSet.as_view({"get": "list", "post": "create"}),
        name="visit_list",
    ),
    path(
        "visits/<int:pk>/",
        VisitViewSet.as_view(
            {
                "get": "retrieve",
                "put": "update",
                "patch": "partial_update",
                "delete": "destroy",
            }
        ),
        name="visit_detail",
    ),
    path(
        "operations/",
        OperationViewSet.as_view({"get": "list", "post": "create"}),
        name="operation_list",
    ),
    path(
        "operations/<int:pk>/",
        OperationViewSet.as_view(
            {
                "get": "retrieve",
                "put": "update",
                "patch": "partial_update",
                "delete": "destroy",
            }
        ),
        name="operation_detail",
    ),
]
