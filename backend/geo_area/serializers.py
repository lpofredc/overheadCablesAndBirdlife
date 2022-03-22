from rest_framework.serializers import ModelSerializer
from rest_framework_gis.serializers import GeoFeatureModelSerializer
from sinp_nomenclatures.serializers import NomenclatureSerializer

from .models import GeoArea


class GeoAreaSerializer(ModelSerializer):
    """Serializer for GeoArea model"""

    type = NomenclatureSerializer()

    class Meta:
        model = GeoArea
        fields = ["id", "name", "code", "type"]


class GeoAreaGeoSerializer(GeoFeatureModelSerializer):
    """Serializer for GeoArea model"""

    type = NomenclatureSerializer()

    class Meta:
        model = GeoArea
        geo_field = "geom"
        fields = ["id", "name", "code", "geom", "type"]
