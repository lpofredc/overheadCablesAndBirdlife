from rest_framework import viewsets
from rest_framework.permissions import DjangoModelPermissions

from .models import SensitiveArea
from .serializers import SensitiveAreaSerializer


class SensitiveAreaViewSet(viewsets.ModelViewSet):
    """A simple viewset to retrieve all the SensitiveArea items"""

    serializer_class = SensitiveAreaSerializer
    permission_classes = [DjangoModelPermissions]
    queryset = SensitiveArea.objects.all()
