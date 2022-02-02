from rest_framework.serializers import ModelSerializer

from .models import Mortality, Species


class SpeciesSerializer(ModelSerializer):
    """Serializer for Mortality model"""

    class Meta:
        model = Species
        fields = ["id", "code", "scientific_name", "vernacular_name", "status"]


class MortalitySerializer(ModelSerializer):
    """Serializer for Mortality model"""

    class Meta:
        model = Mortality
        fields = "__all__"
