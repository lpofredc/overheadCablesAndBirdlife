from rest_framework.serializers import ModelSerializer

from .models import Media


class MediaSerializer(ModelSerializer):
    """Serializer for Media model"""

    class Meta:
        model = Media
        fields = ["id", "storage", "date", "author", "source", "remark"]
