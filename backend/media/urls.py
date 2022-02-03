from django.urls import path

from .views import MediaViewSet

app_name = "media"

urlpatterns = [
    path(
        "",
        MediaViewSet.as_view({"get": "list", "post": "create"}),
        name="media_list",
    ),
    path(
        "<int:pk>/",
        MediaViewSet.as_view(
            {
                "get": "retrieve",
                "patch": "update",
                "put": "partial_update",
                "delete": "destroy",
            }
        ),
        name="media_detail",
    ),
]
