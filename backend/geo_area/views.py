from rest_framework import viewsets
from rest_framework.permissions import DjangoModelPermissions

from .models import GeoArea
from .serializers import GeoAreaSerializer


class GeoAreaViewSet(viewsets.ModelViewSet):
    """A simple viewset to retrieve all the GeoArea items"""

    serializer_class = GeoAreaSerializer
    permission_classes = [DjangoModelPermissions]
    queryset = GeoArea.objects.all()
