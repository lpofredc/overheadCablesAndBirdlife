from django.urls import path

from .views import (
    PoleViewSetEdit,
    PoleViewSetInfo,
    SegmentViewSetEdit,
    SegmentViewSetInfo,
)

urlpatterns = [
    path(
        "poles/info/",
        PoleViewSetInfo.as_view({"get": "list"}),
        name="pole_list_info",
    ),
    path(
        "poles/edit/",
        PoleViewSetEdit.as_view(
            {
                "get": "list",
                "post": "create",
                "put": "update",
                "patch": "partial_update",
            }
        ),
        name="pole_list_edit",
    ),
    path(
        "poles/info/<int:pk>/",
        PoleViewSetInfo.as_view({"get": "retrieve"}),
        name="pole_info",
    ),
    path(
        "poles/edit/<int:pk>/",
        PoleViewSetEdit.as_view(
            {
                "get": "retrieve",
                "put": "update",
                "patch": "partial_update",
                "delete": "destroy",
            }
        ),
        name="pole_edit",
    ),
    path(
        "segments/info/",
        SegmentViewSetInfo.as_view({"get": "list"}),
        name="segments_list_info",
    ),
    path(
        "segments/edit/",
        SegmentViewSetEdit.as_view(
            {
                "get": "list",
                "post": "create",
                "put": "update",
                "patch": "partial_update",
            }
        ),
        name="segments_list_edit",
    ),
    path(
        "segments/info/<int:pk>/",
        SegmentViewSetInfo.as_view({"get": "retrieve"}),
        name="segments_info",
    ),
    path(
        "segments/edit/<int:pk>/",
        SegmentViewSetEdit.as_view(
            {
                "get": "retrieve",
                "put": "update",
                "patch": "partial_update",
                "delete": "destroy",
            }
        ),
        name="segments_edit",
    ),
]
