from django_filters import rest_framework as filters

from .models import Equipment


class EquipmentFilter(filters.FilterSet):
    """Filter for both types of Equipment instances (Pole & Segment)

    If no value given for "pole" (and/or "segment") parameter (get parameters), no filter will be applied to Poles (and/or Segment) all instances will be returned with result"""

    class Meta:
        model = Equipment
        fields = ["installed"]


class PoleEquipmentFilter(filters.FilterSet):
    """Filter for Pole Equipment instances"""

    class Meta:
        model = Equipment
        fields = ["pole", "installed"]


class SegmentEquipmentFilter(filters.FilterSet):
    """Filter for Segment Equipment instances"""

    class Meta:
        model = Equipment
        fields = ["segment", "installed"]
