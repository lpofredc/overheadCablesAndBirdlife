from rest_framework_gis.serializers import (
    GeoFeatureModelSerializer,
    ModelSerializer,
)
from sinp_nomenclatures.serializers import ItemSerializer

from geo_area.serializers import GeoAreaSerializer
from sensitive_area.serializers import SensitiveAreaSerializer

from .models import Operation, Pole, Segment, Visit


class PoleSerializerInfo(GeoFeatureModelSerializer):
    """Serializer for Pole model

    Allow to get all data from pole(including nested) but not allow create and update"""

    owner = ItemSerializer()
    geo_area = GeoAreaSerializer(many=True)
    sensitive_area = SensitiveAreaSerializer(many=True)

    class Meta:
        model = Pole
        geo_field = "geom"
        fields = ["id", "geom", "owner", "geo_area", "sensitive_area"]


class PoleSerializerEdit(GeoFeatureModelSerializer):
    """Serializer for Pole model

    Allow to get data from pole(not nested data, only FK) but allow create and update"""

    class Meta:
        model = Pole

        geo_field = "geom"
        fields = ["id", "geom", "owner", "geo_area", "sensitive_area"]


class SegmentSerializerInfo(ModelSerializer):
    """Serializer for Segment model

    Allow to get all data from segments(including nested) but not allow create and update"""

    owner = ItemSerializer()
    geo_area = GeoAreaSerializer(many=True)
    sensitive_area = SensitiveAreaSerializer(many=True)

    class Meta:
        model = Segment
        fields = ["id", "geom", "owner", "geo_area", "sensitive_area"]


class SegmentSerializerEdit(ModelSerializer):
    """Serializer for Segment model

    Allow to get data from pole(not nested data, only FK) but allow create and update"""

    class Meta:
        model = Segment
        fields = ["id", "geom", "owner", "geo_area", "sensitive_area"]


class VisitSerializer(ModelSerializer):
    """Serializer for Visit model"""

    class Meta:
        model = Visit
        fields = "__all__"


class EquipmentSerializer(ModelSerializer):
    """Serializer for Equipment model"""

    class Meta:
        model = Operation
        fields = "__all__"
