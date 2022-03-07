from django.urls import path

from .views import MortalityViewSet

app_name = "mortality"

urlpatterns = [
    path(
        "",
        MortalityViewSet.as_view({"get": "list", "post": "create"}),
        name="mortality_case_list",
    ),
    path(
        "<int:pk>/",
        MortalityViewSet.as_view(
            {
                "get": "retrieve",
                "put": "update",
                "patch": "partial_update",
                "delete": "destroy",
            }
        ),
        name="mortality_case_detail",
    ),
]
