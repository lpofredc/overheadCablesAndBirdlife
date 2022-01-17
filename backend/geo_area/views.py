from rest_framework import viewsets

from .models import GeoArea
from .serializers import GeoAreaGeoSerializer, GeoAreaSerializer

# from rest_framework.permissions import IsAuthenticated


class GeoAreaViewSet(viewsets.ModelViewSet):
    """A simple viewset to retrieve all the GeoArea items"""

    serializer_class = GeoAreaSerializer
    # permission_classes = [IsAuthenticated]
    queryset = GeoArea.objects.all()


class GeoAreaGeoViewSet(viewsets.ModelViewSet):
    """A simple viewset to retrieve all the GeoArea items"""

    serializer_class = GeoAreaGeoSerializer
    # permission_classes = [IsAuthenticated]
    queryset = GeoArea.objects.all()
