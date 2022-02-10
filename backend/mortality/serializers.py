from rest_framework_gis.serializers import GeoFeatureModelSerializer

from cables.serializers import InfrastructureSerializer
from species.serializers import SpeciesSerializer

from .models import Mortality


class MortalitySerializer(GeoFeatureModelSerializer):
    """Serializer for Mortality

    Used to serialize all data from mortality cases.
    """

    # Allow to display nested data
    species = SpeciesSerializer(read_only=True)
    infrstr = InfrastructureSerializer(read_only=True)

    class Meta:
        model = Mortality
        geo_field = "geom"
        fields = [
            "id",
            "geom",
            "date",
            "species",
            "species_id",
            "infrstr",
            "infrstr_id",
            "nb_death",
            "author",
            "data_source",
            "created_by",
            "media",
        ]
        # Allow to handle create/update/partial_update with nested data
        extra_kwargs = {
            "species_id": {"source": "species", "write_only": True},
            "infrstr_id": {"source": "infrstr", "write_only": True},
        }
