from rest_framework.serializers import ModelSerializer

from .models import Species


class SpeciesSerializer(ModelSerializer):
    """Serializer for Species model"""

    class Meta:
        model = Species
        fields = ["id", "code", "scientific_name", "vernacular_name", "active"]
