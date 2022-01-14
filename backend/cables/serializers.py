from rest_framework.serializers import ModelSerializer

from .models import Equipment, Observation, Pole, Segment


class PoleSerializer(ModelSerializer):
    """Serializer for Pole model"""

    class Meta:
        model = Pole
        fields = "__all__"


class SegmentSerializer(ModelSerializer):
    """Serializer for Segment model"""

    class Meta:
        model = Segment
        fields = "__all__"


class ObservationSerializer(ModelSerializer):
    """Serializer for Observation model"""

    class Meta:
        model = Observation
        fields = "__all__"


class EquipmentSerializer(ModelSerializer):
    """Serializer for Equipment model"""

    class Meta:
        model = Equipment
        fields = "__all__"
