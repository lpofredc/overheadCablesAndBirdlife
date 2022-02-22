import logging

from rest_framework import viewsets
from rest_framework.permissions import DjangoModelPermissions

from .filters import (  # , PoleFilter, SegmentFilter, VisitFilter
    InfrastructureFilter,
    OperationFilter,
)
from .models import Action, Diagnosis, Infrastructure, Line, Operation, Point
from .serializers import (
    ActionPolymorphicSerializer,
    DiagnosisSerializer,
    InfrastructurePolymorphicSerializer,
    LineSerializer,
    OperationSerializer,
    PointSerializer,
)

logger = logging.getLogger(__name__)


class InfrastructureViewSet(viewsets.ModelViewSet):
    """ViewSet for Infrastructure item"""

    serializer_class = InfrastructurePolymorphicSerializer
    permission_classes = [DjangoModelPermissions]
    queryset = Infrastructure.objects.all()
    filterset_class = InfrastructureFilter


class PointViewSet(viewsets.ModelViewSet):
    """ViewSet for Point item"""

    serializer_class = PointSerializer
    permission_classes = [DjangoModelPermissions]
    queryset = Point.objects.all()
    # filterset_class = PointFilter


class LineViewSet(viewsets.ModelViewSet):
    """ViewSet for Line item"""

    serializer_class = LineSerializer
    permission_classes = [DjangoModelPermissions]
    queryset = Line.objects.all()
    # filterset_class = LineFilter


class ActionViewSet(viewsets.ModelViewSet):
    """ViewSet for Action item"""

    serializer_class = ActionPolymorphicSerializer
    permission_classes = [DjangoModelPermissions]
    queryset = Action.objects.all()


class DiagnosisViewSet(viewsets.ModelViewSet):
    """ViewSet for Diagnosis item"""

    serializer_class = DiagnosisSerializer
    permission_classes = [DjangoModelPermissions]
    queryset = Diagnosis.objects.all()


class OperationViewSet(viewsets.ModelViewSet):
    """ViewSet for Operation item"""

    serializer_class = OperationSerializer
    permission_classes = [DjangoModelPermissions]
    queryset = Operation.objects.all()
    filterset_class = OperationFilter
