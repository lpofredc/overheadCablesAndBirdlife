from django.urls import path
from rest_framework import routers

from .views import MediaViewSet

app_name = "media"

router = routers.SimpleRouter()
router.register(r"pictures", MediaViewSet)
urlpatterns = router.urls

urlpatterns = [
    path(
        "list/",
        MediaViewSet.as_view({"get": "list", "post": "create"}),
        name="media_list",
    ),
]
