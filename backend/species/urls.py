from django.urls import path

from .views import SpeciesViewSet

app_name = "species"

urlpatterns = [
    path(
        "",
        SpeciesViewSet.as_view({"get": "list", "post": "create"}),
        name="species_list",
    ),
    path(
        "<int:pk>/",
        SpeciesViewSet.as_view(
            {
                "get": "retrieve",
                "put": "update",
                "patch": "partial_update",
                "delete": "destroy",
            }
        ),
        name="species_detail",
    ),
]
