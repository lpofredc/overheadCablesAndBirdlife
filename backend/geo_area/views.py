from rest_framework import viewsets
from rest_framework.permissions import DjangoModelPermissions

from .models import GeoArea
from .serializers import GeoAreaGeoSerializer


class GeoAreaViewSet(viewsets.ModelViewSet):
    """A simple viewset to retrieve all the GeoArea items"""

    serializer_class = GeoAreaGeoSerializer
    permission_classes = [DjangoModelPermissions]
    queryset = GeoArea.objects.all()
