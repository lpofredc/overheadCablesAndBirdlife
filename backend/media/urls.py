from django.urls import include, path
from rest_framework import routers

from .views import PictureViewSet

app_name = "media"

router = routers.SimpleRouter()
router.register(r"pictures", PictureViewSet)
urlpatterns = router.urls

urlpatterns = [
    path("", include(router.urls)),
]
