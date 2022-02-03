from rest_framework_gis.serializers import GeoFeatureModelSerializer

from species.serializers import SpeciesSerializer

from .models import Mortality


class MortalitySerializer(GeoFeatureModelSerializer):
    """Serializer for Mortality

    Used to serialize all data from mortality cases.
    """

    species = SpeciesSerializer()

    class Meta:
        model = Mortality
        fields = [
            "id",
            "geom",
            "date",
            "species",
            "nb_death",
            "author",
            "data_source",
            "created_by",
            "media",
        ]


class MortalityWriteSerializer(GeoFeatureModelSerializer):
    """Serializer for Mortality: used for creation and updating

    Used to serialize all data from mortality cases.
    """

    class Meta:
        model = Mortality
        fields = [
            "id",
            "geom",
            "date",
            "species",
            "nb_death",
            "author",
            "data_source",
            "created_by",
            "media",
        ]
