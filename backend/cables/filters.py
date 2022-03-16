from django_filters import rest_framework as filters

from commons.models import BaseModel

from .models import Infrastructure, Operation  # , Diagnosis, Line, Point


class BaseModelFilter(filters.FilterSet):
    """Filter for both BaseModel instances

    class BaseModelFilter(filters.FilterSet):
    Filters for all Model classes that herit from BaseModel can herit from this BaseModelFilter class.
    Allowed filters:
    - by creator id of the object => created_by_id
    - by creator of the object => created_by (exact match)
    """

    created_by_id = filters.NumberFilter(field_name="created_by")
    created_by = filters.CharFilter(field_name="created_by__username")

    class Meta:
        model = BaseModel
        fields = []


# class PointFilter(BaseModelFilter):
#     """Filter for Point Infrastructure instances

#     Herits from BaseModelFilter (refer related doc).
#     Allowed filters:
#     - by owner of the object => created_by (owner id)
#     """

#     owner_id = filters.NumberFilter(field_name="owner")

#     class Meta:
#         model = Point
#         fields = {"owner_id": ["exact"]}


# class LineFilter(BaseModelFilter):
#     """Filter for Line instances

#     Herits from BaseModelFilter (refer related doc).
#     Allowed filters:
#     - by owner of the object => created_by (owner id)
#     """

#     owner_id = filters.NumberFilter(field_name="owner")

#     class Meta:
#         model = Line
#         fields = {"owner_id": ["exact"]}


# class DiagnosisFilter(BaseModelFilter):
#     """Filter for Diagnosis instances:

#     Herits from BaseModelFilter (refer related doc).
#     Allowed filters:
#     - by infrastructure id => pole_id or segment_id
#     - by type of infrastructure => is_pole = True/False or is_segment = True/False
#     - by diagnosis_date => date (exact match), from_date (date_gte), to_date (date_lte)
#     - by year of diagnosis_date => year (exact match), from_year (date_gte), to_year (date_lte)
#     - by condition id => condition_id
#     - by pole typeid => pole_type_id
#     """

#     date = filters.DateFilter(field_name="diagnosis_date", lookup_expr="date")
#     from_date = filters.DateFilter(field_name="diagnosis_date", lookup_expr="date__gte")
#     to_date = filters.DateFilter(field_name="diagnosis_date", lookup_expr="date__lte")
#     year = filters.NumberFilter(field_name="diagnosis_date", lookup_expr="year")
#     from_year = filters.NumberFilter(field_name="diagnosis_date", lookup_expr="year__gte")
#     to_year = filters.NumberFilter(field_name="diagnosis_date", lookup_expr="year__lte")
#     condition_id = filters.NumberFilter(field_name="condition__id")
#     pole_type_id = filters.NumberFilter(field_name="pole_type__id")

#     class Meta:
#         model = Diagnosis
#         fields = ["neutralized"]


class OperationFilter(BaseModelFilter):
    """Filter for Operation instances:

    Herits from BaseModelFilter (refer related doc).
    Allowed filters:
    - by infrastructure id => pole_id or segment_id
    - by type of infrastructure => is_pole = True/False or is_segment = True/False
    - by diagnosis_date => diagnosis_date (exact match), from_diagnosis_date (date_gte), to_diagnosis_date (date_lte)
    - by year of operation_date => year (exact match), from_year (date_gte), to_year (date_lte)
    - by condition id => condition_id
    - by pole typeid => pole_type_id
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


class InfrastructureFilter(BaseModelFilter):

    type = filters.NumberFilter(field_name="polymorphic_ctype")
    # is_segment = filters.BooleanFilter(field_name="pole__id", lookup_expr="isnull")
    # date = filters.DateFilter(field_name="operation_date", lookup_expr="date")
    # from_date = filters.DateFilter(field_name="operation_date", lookup_expr="date__gte")
    # to_date = filters.DateFilter(field_name="operation_date", lookup_expr="date__lte")
    # eqmt_type = filters.NumberFilter(field_name="eqmt_type__id")
    # year = filters.NumberFilter(field_name="operation_date", lookup_expr="year")
    # from_year = filters.NumberFilter(field_name="operation_date", lookup_expr="year__gte")
    # to_year = filters.NumberFilter(field_name="operation_date", lookup_expr="year__lte")

    class Meta:
        model = Infrastructure
        fields = ["type"]
