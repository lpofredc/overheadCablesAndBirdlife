from rest_framework import viewsets

from .models import Species
from .serializers import SpeciesSerializer

# from rest_framework.permissions import (
#     IsAuthenticated,  # DjangoModelPermissions,
# )


class SpeciesViewSet(viewsets.ModelViewSet):
    """ViewSet for Species items"""

    serializer_class = SpeciesSerializer
    # permission_classes = [DjangoModelPermissions]
    queryset = Species.objects.all()
