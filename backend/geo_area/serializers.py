from rest_framework.serializers import ModelSerializer
from rest_framework_gis.serializers import GeoFeatureModelSerializer

from .models import GeoArea


class GeoAreaGeoSerializer(ModelSerializer):
    """Serializer for GeoArea model"""

    class Meta:
        model = GeoArea
        fields = ["id", "name", "code"]


class GeoAreaSerializer(GeoFeatureModelSerializer):
    """Serializer for GeoArea model"""

    class Meta:
        model = GeoArea
        geo_field = "geom"
        fields = ["id", "name", "code", "geom"]
