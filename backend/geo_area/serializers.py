from rest_framework_gis.serializers import ModelSerializer

from .models import GeoArea


class GeoAreaSerializer(ModelSerializer):
    """Serializer for GeoArea model"""

    class Meta:
        model = GeoArea
        fields = ["id", "name", "code"]
