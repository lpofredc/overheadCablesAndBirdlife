from django.urls import path

from .views import PingView

app_name = "commons"

urlpatterns = [
    path(
        "ping",
        PingView.as_view(),
        name="ping",
    ),
]
