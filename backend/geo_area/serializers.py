from rest_framework_gis.serializers import (
    GeoFeatureModelSerializer,
    ModelSerializer,
)

from .models import GeoArea


class GeoAreaGeoSerializer(GeoFeatureModelSerializer):
    """Serializer for GeoArea model"""

    class Meta:
        model = GeoArea
        geo_field = "geom"
        fields = ["id", "name", "code", "geom"]


class GeoAreaSerializer(ModelSerializer):
    """Serializer for GeoArea model"""

    class Meta:
        model = GeoArea
        fields = ["id", "name", "code"]
