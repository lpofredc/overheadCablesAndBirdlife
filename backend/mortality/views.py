from rest_framework import viewsets

from .models import Mortality
from .serializers import MortalitySerializer

# from rest_framework.permissions import (
#     IsAuthenticated,  # DjangoModelPermissions,
# )


class MortalityViewSet(viewsets.ModelViewSet):
    """ViewSet for Mortality item"""

    serializer_class = MortalitySerializer
    # permission_classes = [IsAuthenticated]
    queryset = Mortality.objects.all()
