from rest_framework.serializers import ModelSerializer

from .models import Equipment, Pole, Segment, Visit


class PoleSerializer(ModelSerializer):
    """Serializer for Pole model"""

    class Meta:
        model = Pole
        fields = "__all__"
        depth = 1


class SegmentSerializer(ModelSerializer):
    """Serializer for Segment model"""

    class Meta:
        model = Segment
        fields = "__all__"


class VisitSerializer(ModelSerializer):
    """Serializer for Visit model"""

    class Meta:
        model = Visit
        fields = "__all__"


class EquipmentSerializer(ModelSerializer):
    """Serializer for Equipment model"""

    class Meta:
        model = Equipment
        fields = "__all__"
