from rest_framework_gis.serializers import GeoFeatureModelSerializer

from .models import GeoArea


class GeoAreaSerializer(GeoFeatureModelSerializer):
    """Serializer for GeoArea model"""

    class Meta:
        model = GeoArea
        geo_field = "geom"
        fields = ["id", "name", "code", "geom"]
