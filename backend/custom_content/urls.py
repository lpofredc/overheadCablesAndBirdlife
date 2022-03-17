from django.urls import path

from .views import NewsFullViewSet, NewsSimpleViewSet, PartnersViewSet

app_name = "custom_content"

urlpatterns = [
    path(
        "news/",
        NewsSimpleViewSet.as_view({"get": "list", "post": "create"}),
        name="news_list",
    ),
    path(
        "news/<int:pk>/",
        NewsFullViewSet.as_view({"get": "retrieve"}),
        name="news_detail",
    ),
    path(
        "partners/",
        PartnersViewSet.as_view({"get": "list"}),
        name="partners_list",
    ),
]
