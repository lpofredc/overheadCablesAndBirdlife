from django.urls import path

from .views import SpeciesViewSet  # MortalityViewSet,

app_name = "mortality"

urlpatterns = [
    path(
        "species/",
        SpeciesViewSet.as_view({"get": "list", "post": "create"}),
        name="species_list",
    ),
    path(
        "species/<int:pk>/",
        SpeciesViewSet.as_view(
            {
                "get": "retrieve",
                "put": "update",
                "patch": "partial_update",
            }
        ),
        name="species_detail",
    ),
]
