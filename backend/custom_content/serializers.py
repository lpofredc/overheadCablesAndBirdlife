from rest_framework.serializers import ModelSerializer

from users.serializers import UserSimpleSerializer

from .models import News, Partners


class NewsSimpleSerializer(ModelSerializer):
    """Serializer for News model"""

    created_by = UserSimpleSerializer()
    updated_by = UserSimpleSerializer()

    class Meta:
        model = News
        fields = [
            "id",
            "title",
            "intro",
            "timestamp_create",
            "created_by",
            "timestamp_update",
            "updated_by",
        ]


class NewsFullSerializer(ModelSerializer):
    """Serializer for News model"""

    created_by = UserSimpleSerializer()
    updated_by = UserSimpleSerializer()

    class Meta:
        model = News
        fields = [
            "id",
            "title",
            "intro",
            "timestamp_create",
            "created_by",
            "timestamp_update",
            "updated_by",
            "body",
        ]


class PartnersSerializer(ModelSerializer):
    """Serializer for News model"""

    class Meta:
        model = Partners
        fields = [
            "id",
            "name",
            "short_name",
            "url",
            "logo",
        ]
