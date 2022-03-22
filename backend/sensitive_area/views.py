from rest_framework import viewsets
from rest_framework.permissions import DjangoModelPermissions

from .models import SensitiveArea
from .serializers import SensitiveAreaGeoSerializer


class SensitiveAreaViewSet(viewsets.ModelViewSet):
    """A simple viewset to retrieve all the SensitiveArea items"""

    serializer_class = SensitiveAreaGeoSerializer
    permission_classes = [DjangoModelPermissions]
    queryset = SensitiveArea.objects.all()
