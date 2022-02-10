import logging

from rest_framework import viewsets
from rest_framework.permissions import DjangoModelPermissions

# from .filters import OperationFilter, PoleFilter, SegmentFilter, VisitFilter
from .models import Action, Infrastructure, Operation, Pole, Segment, Visit
from .serializers import (
    ActionPolymorphicSerializer,
    InfrastructurePolymorphicSerializer,
    OperationSerializer,
    PoleSerializer,
    SegmentSerializer,
    VisitSerializer,
)

logger = logging.getLogger(__name__)


class InfrastructureViewSet(viewsets.ModelViewSet):
    """ViewSet for Infrastructure item"""

    serializer_class = InfrastructurePolymorphicSerializer
    permission_classes = [DjangoModelPermissions]
    queryset = Infrastructure.objects.all()
    # filterset_class = PoleFilter


class PoleViewSet(viewsets.ModelViewSet):
    """ViewSet for Pole item"""

    serializer_class = PoleSerializer
    permission_classes = [DjangoModelPermissions]
    queryset = Pole.objects.all()
    # filterset_class = PoleFilter


class SegmentViewSet(viewsets.ModelViewSet):
    """ViewSet for Segment item"""

    serializer_class = SegmentSerializer
    permission_classes = [DjangoModelPermissions]
    queryset = Segment.objects.all()
    # filterset_class = SegmentFilter


class ActionViewSet(viewsets.ModelViewSet):
    """ViewSet for Action item"""

    serializer_class = ActionPolymorphicSerializer
    permission_classes = [DjangoModelPermissions]
    queryset = Action.objects.all()
    # filterset_class = SegmentFilter


class VisitViewSet(viewsets.ModelViewSet):
    """ViewSet for Visit item"""

    serializer_class = VisitSerializer
    permission_classes = [DjangoModelPermissions]
    queryset = Visit.objects.all()
    # filterset_class = SegmentFilter


class OperationViewSet(viewsets.ModelViewSet):
    """ViewSet for Operation item"""

    serializer_class = OperationSerializer
    permission_classes = [DjangoModelPermissions]
    queryset = Operation.objects.all()
    # filterset_class = SegmentFilter
