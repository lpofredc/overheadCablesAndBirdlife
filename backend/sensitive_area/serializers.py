from rest_framework.serializers import ModelSerializer

from .models import SensitiveArea


class SensitiveAreaSerializer(ModelSerializer):
    """Serializer for SensitiveArea model"""

    class Meta:
        model = SensitiveArea
        fields = "__all__"
