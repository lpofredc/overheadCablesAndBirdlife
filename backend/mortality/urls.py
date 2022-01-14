from django.urls import include, path
from rest_framework import routers

from .views import MortalityViewSet

app_name = "mortality"

router = routers.SimpleRouter()
router.register(r"entries", MortalityViewSet)
urlpatterns = router.urls

urlpatterns = [
    path("", include(router.urls)),
]
