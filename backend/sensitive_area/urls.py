from django.urls import path

from .views import SensitiveAreaViewSet

app_name = "sensitive_area"


urlpatterns = [
    path(
        "",
        SensitiveAreaViewSet.as_view({"get": "list", "post": "create"}),
        name="sensitivearea-list",
    ),
    path(
        "<int:pk>/",
        SensitiveAreaViewSet.as_view(
            {
                "get": "retrieve",
                "put": "update",
                "patch": "partial_update",
                "delete": "destroy",
            }
        ),
        name="sensitivearea-detail",
    ),
]
