from rest_framework.serializers import ModelSerializer

from .models import GeoArea


class GeoAreaSerializer(ModelSerializer):
    """Serializer for GeoArea model"""

    class Meta:
        model = GeoArea
        fields = "__all__"
        depth = 1
