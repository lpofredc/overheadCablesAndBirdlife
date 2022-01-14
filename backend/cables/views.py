from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Equipment, Observation, Pole, Segment
from .serializers import (
    EquipmentSerializer,
    ObservationSerializer,
    PoleSerializer,
    SegmentSerializer,
)


class PoleViewSet(viewsets.ModelViewSet):
    """A simple viewset to retrieve all the Pole items"""

    serializer_class = PoleSerializer
    permission_classes = [IsAuthenticated]
    queryset = Pole.objects.all()


class SegmentViewSet(viewsets.ModelViewSet):
    """A simple viewset to retrieve all the Segment items"""

    serializer_class = SegmentSerializer
    # permission_classes = [IsAuthenticated]
    queryset = Segment.objects.all()


class ObservationViewSet(viewsets.ModelViewSet):
    """A simple viewset to retrieve all the Observation items"""

    serializer_class = ObservationSerializer
    # permission_classes = [IsAuthenticated]
    queryset = Observation.objects.all()


class EquipmentViewSet(viewsets.ModelViewSet):
    """A simple viewset to retrieve all the Observation items"""

    serializer_class = EquipmentSerializer
    # permission_classes = [IsAuthenticated]
    queryset = Equipment.objects.all()
