from rest_framework import viewsets

from .models import Mortality
from .serializers import MortalitySerializer, MortalityWriteSerializer

# from rest_framework.permissions import (
#     IsAuthenticated,  # DjangoModelPermissions,
# )


class MortalityViewSet(viewsets.ModelViewSet):
    """ViewSet for Mortality item"""

    serializer_class = MortalitySerializer
    # permission_classes = [IsAuthenticated]
    queryset = Mortality.objects.all()

    def get_serializer_class(self):
        """Method that select appropriate serializer depending on request method

        Returns:
            [Serializer]: return appropriate serializer depending on request method.
        """
        serializer = {
            "GET": MortalitySerializer,
            "PATCH": MortalityWriteSerializer,
            "PUT": MortalityWriteSerializer,
            "POST": MortalityWriteSerializer,
        }
        return serializer[self.request.method]
