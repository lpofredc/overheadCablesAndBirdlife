from django.urls import path

from .views import PoleFullVieweSet, PoleViewSet

urlpatterns = [
    path(
        "poles/info",
        PoleFullVieweSet.as_view({"get": "list"}),
        name="pole_list_info",
    ),
    path(
        "poles/edit",
        PoleViewSet.as_view(
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
        PoleFullVieweSet.as_view({"get": "retrieve"}),
        name="pole_info",
    ),
    path(
        "poles/edit/<int:pk>/",
        PoleViewSet.as_view(
            {
                "get": "retrieve",
                "put": "update",
                "patch": "partial_update",
                "delete": "destroy",
            }
        ),
        name="pole_edit",
    ),
]
