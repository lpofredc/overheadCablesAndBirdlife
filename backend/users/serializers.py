from rest_framework.serializers import ModelSerializer

from .models import User


class UserSimpleSerializer(ModelSerializer):
    """Serializer for Media model"""

    class Meta:
        model = User
        fields = [
            "username",
            "full_name",
            "avatar",
        ]
