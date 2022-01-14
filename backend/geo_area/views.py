from rest_framework import viewsets

from .models import GeoArea
from .serializers import GeoAreaSerializer

# from rest_framework.permissions import IsAuthenticated


class GeoAreaViewSet(viewsets.ModelViewSet):
    """A simple viewset to retrieve all the GeoArea items"""

    serializer_class = GeoAreaSerializer
    # permission_classes = [IsAuthenticated]
    queryset = GeoArea.objects.all()
