from rest_framework.serializers import ModelSerializer
from rest_framework_gis.serializers import GeoFeatureModelSerializer

from .models import SensitiveArea


class SensitiveAreaSerializer(ModelSerializer):
    """Serializer for SensitiveArea model"""

    class Meta:
        model = SensitiveArea
        fields = ["id", "name", "code"]


class SensitiveAreaGeoSerializer(GeoFeatureModelSerializer):
    """Serializer for SensitiveArea model"""

    class Meta:
        model = SensitiveArea
        geo_field = "geom"
        fields = ["id", "name", "code", "geom"]
