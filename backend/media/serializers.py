from rest_framework.serializers import ModelSerializer

from .models import Picture


class PictureSerializer(ModelSerializer):
    """Serializer for Picture model"""

    class Meta:
        model = Picture
        fields = "__all__"
