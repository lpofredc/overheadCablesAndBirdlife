from rest_framework import viewsets
from rest_framework.permissions import (
    IsAuthenticated,  # DjangoModelPermissions,
)

from mortality.serializers import SpeciesSerializer

from .models import Mortality, Species
from .serializers import MortalitySerializer


class SpeciesViewSet(viewsets.ModelViewSet):
    """A simple viewset to handle all the Species items"""

    serializer_class = SpeciesSerializer
    # permission_classes = [DjangoModelPermissions]
    queryset = Species.objects.all()


class MortalityViewSet(viewsets.ModelViewSet):
    """A simple viewset to handle all the Mortality items"""

    serializer_class = MortalitySerializer
    permission_classes = [IsAuthenticated]
    queryset = Mortality.objects.all()
