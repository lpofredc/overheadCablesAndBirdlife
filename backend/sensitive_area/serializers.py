from rest_framework_gis.serializers import GeoFeatureModelSerializer

from .models import SensitiveArea


class SensitiveAreaSerializer(GeoFeatureModelSerializer):
    """Serializer for SensitiveArea model"""

    class Meta:
        model = SensitiveArea
        geo_field = "geom"
        fields = ["id", "name", "code", "geom"]
