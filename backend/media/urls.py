from django.urls import include, path
from rest_framework import routers

from .views import MediaViewSet

app_name = "media"

router = routers.SimpleRouter()
router.register(r"pictures", MediaViewSet)
urlpatterns = router.urls

urlpatterns = [
    path("", include(router.urls)),
]
