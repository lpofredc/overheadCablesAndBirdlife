from django.urls import include, path

from cables.mortality_case import urls as mortality_case_urls

app_name = "mortality_case"

urlpatterns = [
    path("", include(mortality_case_urls)),
]
