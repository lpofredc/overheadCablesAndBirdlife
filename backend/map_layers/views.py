from rest_framework import viewsets

from .models import BaseLayers
from .serializers import BaseLayersSerializer

# from rest_framework.permissions import (
#     IsAuthenticated,  # DjangoModelPermissions,
# )


class BaseLayersViewSet(viewsets.ModelViewSet):
    """ViewSet for Mortality item"""

    serializer_class = BaseLayersSerializer
    # permission_classes = [IsAuthenticated]
    queryset = BaseLayers.objects.all()
