from rest_framework_gis.serializers import (
    GeoFeatureModelSerializer,
    ModelSerializer,
)
from sinp_nomenclatures.serializers import ItemSerializer

from geo_area.serializers import GeoAreaSerializer
from media.serializers import MediaSerializer
from sensitive_area.serializers import SensitiveAreaSerializer

from .models import Operation, Pole, Segment, Visit


class PoleSerializerInfo(GeoFeatureModelSerializer):
    """Serializer for Pole model

    Allow to get all data from poles (including nested) but not allow create and update"""

    owner = ItemSerializer()
    geo_area = GeoAreaSerializer(many=True)
    sensitive_area = SensitiveAreaSerializer(many=True)

    class Meta:
        model = Pole
        geo_field = "geom"
        fields = ["id", "geom", "owner", "geo_area", "sensitive_area"]


class PoleSerializerEdit(GeoFeatureModelSerializer):
    """Serializer for Pole model

    Allow to get data from poles (not nested data, only FK) but allow create and update"""

    class Meta:
        model = Pole

        geo_field = "geom"
        fields = ["id", "geom", "owner", "geo_area", "sensitive_area"]


class SegmentSerializerInfo(ModelSerializer):
    """Serializer for Segment model

    Allow to get all data from segments (including nested) but not allow create and update"""

    owner = ItemSerializer()
    geo_area = GeoAreaSerializer(many=True)
    sensitive_area = SensitiveAreaSerializer(many=True)

    class Meta:
        model = Segment
        fields = ["id", "geom", "owner", "geo_area", "sensitive_area"]


class SegmentSerializerEdit(ModelSerializer):
    """Serializer for Segment model

    Allow to get data from segments (not nested data, only FK) but allow create and update"""

    class Meta:
        model = Segment
        fields = ["id", "geom", "owner", "geo_area", "sensitive_area"]


class VisitSerializerInfo(ModelSerializer):
    """Serializer for Visit model

    Allow to get all data from visits (including nested) but not allow create and update"""

    pole = PoleSerializerInfo()
    segment = SegmentSerializerInfo()
    media = MediaSerializer(many=True)
    condition = ItemSerializer()
    # pole_type = PoleTypeSerializer()
    pole_attractivity = ItemSerializer()
    pole_dangerousness = ItemSerializer()
    segt_build_integr_risk = ItemSerializer()
    segt_moving_risk = ItemSerializer()
    gmt_topo_integr_risk = ItemSerializer()
    sgmt_veget_integr_risk = ItemSerializer()

    class Meta:
        model = Visit
        exclude = ["uuid"]


class VisitSerializerEdit(ModelSerializer):
    """Serializer for Vsit model

    Allow to get data from visits (not nested data, only FK) but allow create and update"""

    class Meta:
        model = Visit
        exclude = ["uuid"]


class EquipmentSerializer(ModelSerializer):
    """Serializer for Equipment model"""

    class Meta:
        model = Operation
        fields = "__all__"
