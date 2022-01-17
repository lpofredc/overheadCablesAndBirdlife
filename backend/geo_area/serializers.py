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
        fields = "__all__"
        depth = 1


class GeoAreaSerializer(ModelSerializer):
    """Serializer for GeoArea model"""

    class Meta:
        model = GeoArea
        fields = "__all__"
        depth = 1
