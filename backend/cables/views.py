from rest_framework import viewsets
from rest_framework.permissions import (
    DjangoModelPermissions,  # IsAuthenticated
)

from .filters import (
    EquipmentFilter,
    PoleEquipmentFilter,
    PoleFilter,
    SegmentEquipmentFilter,
)
from .models import Equipment, Pole, Segment, Visit
from .serializers import (
    EquipmentSerializer,
    PoleSerializer,
    SegmentSerializer,
    VisitSerializer,
)


class PoleViewSet(viewsets.ModelViewSet):
    """A simple viewset to retrieve all the Pole items"""

    serializer_class = PoleSerializer
    # permission_classes = [IsAuthenticated]
    queryset = Pole.objects.all()
    filterset_class = PoleFilter


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
    """A simple viewset to retrieve all the Visit items

    If no value given for "pole" (and/or "segment") parameter (get parameters), no filter will be applied to Poles (and/or Segment) all instances will be returned with result"""

    serializer_class = EquipmentSerializer
    permission_classes = [DjangoModelPermissions]
    queryset = Equipment.objects.all()
    filterset_class = EquipmentFilter

    def get_queryset(self):
        pole = self.request.query_params.get("pole")
        segment = self.request.query_params.get("segment")
        pole_qs = self.queryset
        sgmt_qs = self.queryset
        queryset = Equipment.objects.all()
        if pole is not None:
            pole_qs = queryset.filter(pole=pole)
        if segment is not None:
            sgmt_qs = queryset.filter(segment=segment)
        return pole_qs | sgmt_qs


class PoleEquipmentViewSet(viewsets.ModelViewSet):
    """A simple viewset to retrieve all the Visit items"""

    serializer_class = EquipmentSerializer
    permission_classes = [DjangoModelPermissions]
    queryset = Equipment.objects.all()
    filterset_class = PoleEquipmentFilter

    def get_queryset(self):
        return self.queryset.filter(pole__isnull=False)


class SegmentEquipmentViewSet(viewsets.ModelViewSet):
    """A simple viewset to retrieve all the Visit items"""

    serializer_class = EquipmentSerializer
    permission_classes = [DjangoModelPermissions]
    queryset = Equipment.objects.all()
    filterset_class = SegmentEquipmentFilter

    def get_queryset(self):
        return self.queryset.filter(segment__isnull=False)


# class EquipmentViewSet(viewsets.ModelViewSet):
#     """A simple viewset to retrieve all the Visit items"""

#     serializer_class = EquipmentSerializer
#     # permission_classes = [IsAuthenticated]
#     queryset = Equipment.objects.all()
#     filterset_fields = ["installed"]

#     def get_queryset(self):
#         pole = self.kwargs["pole_id"]
#         queryset = Equipment.objects.all()
#         if pole is not None:
#             queryset = queryset.filter(pole__lt=pole)
#         return queryset


# class EquipmentViewSet(viewsets.ModelViewSet):
#     """A simple viewset to retrieve all the Visit items"""

#     serializer_class = EquipmentSerializer
#     # permission_classes = [IsAuthenticated]

#     def get_queryset(self):
#         pole = self.request.query_params.get("pole_id")
#         queryset = Equipment.objects.all()
#         if pole is not None:
#             queryset = queryset.filter(pole=pole)
#         return queryset


# # TEST_TMP
# class EquipmentList(generics.ListAPIView):
#     queryset = Equipment.objects.all()
#     serializer_class = EquipmentSerializer
#     filter_backends = [DjangoFilterBackend]
#     # filterset_fields = ["pole"]
#     filterset_class = EquipmentFilter


# TEST_TMP
# class EquipmentList(generics.ListAPIView):
#     serializer_class = EquipmentSerializer

#     def get_queryset(self):
#         """
#         Optionally restricts the returned purchases to a given user,
#         by filtering against a `username` query parameter in the URL.
#         """
#         queryset = Equipment.objects.all()
#         pole = self.kwargs["pole_id"]
#         if pole is not None:
#             queryset = queryset.filter(pole=pole)
#         return queryset


# TEST_TMP
# class EquipmentList(generics.ListAPIView):
#     serializer_class = EquipmentSerializer

#     def get_queryset(self):
#         """
#         Optionally restricts the returned purchases to a given user,
#         by filtering against a `username` query parameter in the URL.
#         """
#         queryset = Equipment.objects.all()
#         segment = self.request.query_params.get("segment")
#         if segment is not None:
#             queryset = queryset.filter(segment__lt=segment)
#         return queryset
