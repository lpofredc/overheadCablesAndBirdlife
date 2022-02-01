from django_filters import rest_framework as filters

from .models import Operation, Pole, Segment, Visit


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
        model = Pole
        fields = []


class PoleFilter(BaseModelFilter):
    """Filter for both Infrastructure instances: Pole and Segment

    Herits from BaseModelFilter (refer related doc).
    Allowed filters:
    - by owner of the object => created_by (owner id)
    """

    owner_id = filters.NumberFilter(field_name="owner")

    class Meta:
        model = Pole
        fields = {"owner_id": ["exact"]}


class SegmentFilter(BaseModelFilter):
    """Filter for both Infrastructure instances: Pole and Segment

    Herits from BaseModelFilter (refer related doc).
    Allowed filters:
    - by owner of the object => created_by (owner id)
    """

    owner_id = filters.NumberFilter(field_name="owner")

    class Meta:
        model = Segment
        fields = {"owner_id": ["exact"]}


class VisitFilter(BaseModelFilter):
    """Filter for Visit instances:

    Herits from BaseModelFilter (refer related doc).
    Allowed filters:
    - by infrastructure id => pole_id or segment_id
    - by type of infrastructure => is_pole = True/False or is_segment = True/False
    - by visit_date => date (exact match), from_date (date_gte), to_date (date_lte)
    - by year of visit_date => year (exact match), from_year (date_gte), to_year (date_lte)
    - by condition id => condition_id
    - by pole typeid => pole_type_id
    """

    pole = filters.NumberFilter(field_name="pole__id")
    segment = filters.NumberFilter(field_name="segment__id")
    # if segment__id is null => is_pole = true (due to constrainst on model)
    is_pole = filters.BooleanFilter(
        field_name="segment__id", lookup_expr="isnull"
    )
    # if pole__id is null => is_segment = true (due to constrainst on model)
    is_segment = filters.BooleanFilter(
        field_name="pole__id", lookup_expr="isnull"
    )
    date = filters.DateFilter(field_name="visit_date", lookup_expr="date")
    from_date = filters.DateFilter(
        field_name="visit_date", lookup_expr="date__gte"
    )
    to_date = filters.DateFilter(
        field_name="visit_date", lookup_expr="date__lte"
    )
    year = filters.NumberFilter(field_name="visit_date", lookup_expr="year")
    from_year = filters.NumberFilter(
        field_name="visit_date", lookup_expr="year__gte"
    )
    to_year = filters.NumberFilter(
        field_name="visit_date", lookup_expr="year__lte"
    )
    condition_id = filters.NumberFilter(field_name="condition__id")
    pole_type_id = filters.NumberFilter(field_name="pole_type__id")

    class Meta:
        model = Visit
        fields = ["neutralized"]


class OperationFilter(BaseModelFilter):
    """Filter for Operation instances:

    Herits from BaseModelFilter (refer related doc).
    Allowed filters:
    - by infrastructure id => pole_id or segment_id
    - by type of infrastructure => is_pole = True/False or is_segment = True/False
    - by visit_date => visit_date (exact match), from_visit_date (date_gte), to_visit_date (date_lte)
    - by year of operation_date => year (exact match), from_year (date_gte), to_year (date_lte)
    - by condition id => condition_id
    - by pole typeid => pole_type_id
    """

    pole = filters.NumberFilter(field_name="pole__id")
    segment = filters.NumberFilter(field_name="segment__id")
    # if segment__id is null => is_pole = true (due to constrainst on model)
    is_pole = filters.BooleanFilter(
        field_name="segment__id", lookup_expr="isnull"
    )
    # if pole__id is null => is_segment = true (due to constrainst on model)
    is_segment = filters.BooleanFilter(
        field_name="pole__id", lookup_expr="isnull"
    )
    date = filters.DateFilter(field_name="operation_date", lookup_expr="date")
    from_date = filters.DateFilter(
        field_name="operation_date", lookup_expr="date__gte"
    )
    to_date = filters.DateFilter(
        field_name="operation_date", lookup_expr="date__lte"
    )
    eqmt_type = filters.NumberFilter(field_name="eqmt_type__id")
    year = filters.NumberFilter(
        field_name="operation_date", lookup_expr="year"
    )
    from_year = filters.NumberFilter(
        field_name="operation_date", lookup_expr="year__gte"
    )
    to_year = filters.NumberFilter(
        field_name="operation_date", lookup_expr="year__lte"
    )

    class Meta:
        model = Operation
        fields = []


# class EquipmentFilter(filters.FilterSet):
#     """Filter for both types of Equipment instances (Pole & Segment)

#     If no value given for "pole" (and/or "segment") parameter (get parameters), no filter will be applied to Poles (and/or Segment) all instances will be returned with result"""

#     class Meta:
#         model = Operation
#         fields = ["installed"]


# class PoleEquipmentFilter(filters.FilterSet):
#     """Filter for Pole Equipment instances"""

#     class Meta:
#         model = Operation
#         fields = ["pole", "installed"]


# class SegmentEquipmentFilter(filters.FilterSet):
#     """Filter for Segment Equipment instances"""

#     class Meta:
#         model = Operation
#         fields = ["segment", "installed"]
