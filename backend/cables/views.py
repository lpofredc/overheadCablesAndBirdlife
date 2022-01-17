# from django.shortcuts import render

from rest_framework import viewsets

from .models import Equipment, Pole, Segment, Visit
from .serializers import (
    EquipmentSerializer,
    PoleSerializer,
    SegmentSerializer,
    VisitSerializer,
)


class PoleViewSet(viewsets.ModelViewSet):
    """A simple viewset to retrieve all the Pole items"""

    def toto(self, request):
        pass

    serializer_class = PoleSerializer
    # permission_classes = [IsAuthenticated]
    queryset = Pole.objects.all()


class SegmentViewSet(viewsets.ModelViewSet):
    """A simple viewset to retrieve all the Segment items"""

    serializer_class = SegmentSerializer
    # permission_classes = [IsAuthenticated]
    queryset = Segment.objects.all()


class VisitViewSet(viewsets.ModelViewSet):
    """A simple viewset to retrieve all the Visit items"""

    serializer_class = VisitSerializer
    # permission_classes = [IsAuthenticated]
    queryset = Visit.objects.all()


class EquipmentViewSet(viewsets.ModelViewSet):
    """A simple viewset to retrieve all the Visit items"""

    serializer_class = EquipmentSerializer
    # permission_classes = [IsAuthenticated]
    queryset = Equipment.objects.all()
