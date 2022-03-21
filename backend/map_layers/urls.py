from django.urls import path

from .views import BaseLayersViewSet

app_name = "map_layers"

urlpatterns = [
    path(
        "baselayers/",
        BaseLayersViewSet.as_view({"get": "list"}),
        name="base_layers_list",
    ),
]
