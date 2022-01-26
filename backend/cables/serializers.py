# from rest_framework.serializers import ModelSerializer
from rest_framework_gis.serializers import (
    GeoFeatureModelSerializer,
    ModelSerializer,
)
from sinp_nomenclatures.serializers import ItemSerializer

from geo_area.serializers import GeoAreaSerializer
from sensitive_area.serializers import SensitiveAreaSerializer

from .models import Equipment, Pole, Segment, Visit


class PoleSerializer(GeoFeatureModelSerializer):
    """Serializer for Pole model"""

    owner = ItemSerializer()
    geo_area = GeoAreaSerializer(many=True)
    sensitive_area = SensitiveAreaSerializer(many=True)

    class Meta:
        model = Pole
        geo_field = "geom"
        fields = ["id", "geom", "owner", "geo_area", "sensitive_area"]


class PoleSerializerUpd(GeoFeatureModelSerializer):
    """Serializer for Pole model"""

    class Meta:
        model = Pole

        geo_field = "geom"
        fields = ["id", "geom", "owner", "geo_area", "sensitive_area"]


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
