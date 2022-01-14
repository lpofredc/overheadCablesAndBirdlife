from django.urls import include, path
from rest_framework import routers

from .views import SensitiveAreaViewSet

app_name = "sensitive_area"

router = routers.SimpleRouter()
router.register(r"areas", SensitiveAreaViewSet)
urlpatterns = router.urls

urlpatterns = [
    path("", include(router.urls)),
]
