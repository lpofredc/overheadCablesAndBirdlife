from django.urls import path

from .views import PoleViewSetEdit, PoleViewSetInfo

urlpatterns = [
    path(
        "poles/info/",
        PoleViewSetInfo.as_view({"get": "list", "post": "create"}),
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
]
