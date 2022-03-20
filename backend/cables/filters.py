from django_filters import rest_framework as filters

from .models import Diagnosis, Operation


class DiagnosisFilter(filters.FilterSet):
    """Filter for Diagnosis instances:

    Allow to filter on object type (refer django_rest_polymorphique)
    - by infrastructure type id (type) => filter based on polymorphic_ctype_id field of Infrastructure
    - by type model name (type_model) => filter based on model from django content_type table field matching polymorphic_ctype_id in Infrastructure
    """

    type = filters.NumberFilter(
        field_name="infrastructure__polymorphic_ctype_id"
    )
    type_model = filters.CharFilter(
        field_name="infrastructure__polymorphic_ctype__model"
    )

    class Meta:
        model = Diagnosis
        fields = ["type", "type_model"]


class OperationFilter(filters.FilterSet):
    """Filter for Operation instances:

    Allow to filter on object type (refer django_rest_polymorphique)
    - by infrastructure type id (type) => filter based on polymorphic_ctype_id field of Infrastructure
    - by type model name (type_model) => filter based on model from django content_type table field matching polymorphic_ctype_id in Infrastructure
    """

    type = filters.NumberFilter(
        field_name="infrastructure__polymorphic_ctype_id"
    )
    type_model = filters.CharFilter(
        field_name="infrastructure__polymorphic_ctype__model"
    )

    class Meta:
        model = Operation
        fields = ["type", "type_model"]
