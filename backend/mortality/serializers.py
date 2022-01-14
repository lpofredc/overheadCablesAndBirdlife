from rest_framework.serializers import ModelSerializer

from .models import Mortality


class MortalitySerializer(ModelSerializer):
    """Serializer for Mortality model"""

    class Meta:
        model = Mortality
        fields = "__all__"
