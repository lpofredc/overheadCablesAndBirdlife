from django_filters import rest_framework as filters

from .models import Operation, Pole, Segment, Visit


class BaseModelFilter(filters.FilterSet):
    """Filter for both BaseModel instances

    class BaseModelFilter(filters.FilterSet):
    Filters for all Model classes that herit from BaseModel can herit from this BaseModelFilter class.
    Allowed filters:
    - by creator id of the object => created_by_id
    - by creator of the object => created_by (exact match)
    - by date of creation of the object or range of creation date => date (exact match), from_date (date_gte), to_date (date_lte)
    - by year of creation of the object or range of creation date => year (exact macth), from_date (year_gte), to_date (year_lte)
    """

    created_by_id = filters.NumberFilter(field_name="created_by")
    created_by = filters.CharFilter(field_name="created_by__username")
    date = filters.DateFilter(
        field_name="timestamp_create", lookup_expr="date"
    )
    from_date = filters.DateFilter(
        field_name="timestamp_create", lookup_expr="date__gte"
    )
    to_date = filters.DateFilter(
        field_name="timestamp_create", lookup_expr="date__lte"
    )

    year = filters.NumberFilter(
        field_name="timestamp_create", lookup_expr="year"
    )
    from_year = filters.NumberFilter(
        field_name="timestamp_create", lookup_expr="year__gte"
    )
    to_year = filters.NumberFilter(
        field_name="timestamp_create", lookup_expr="year__lte"
    )

    class Meta:
        model = Pole
        fields = [
            "created_by_id",
            "created_by",
            "year",
            "from_year",
            "to_year",
            "date",
            "from_date",
            "to_date",
        ]


class PoleFilter(BaseModelFilter):
    """Filter for both Infrastructure instances: Pole and Segment

    Herits from BaseModelFilter (refer related doc).
    Allowed filters:
    - by organism owner of the object => created_by (owner id)
    """

    owner_id = filters.NumberFilter(field_name="owner")

    class Meta:
        model = Pole
        fields = {"owner_id": ["exact"]}


class SegmentFilter(BaseModelFilter):
    """Filter for both Infrastructure instances: Pole and Segment

    Herits from BaseModelFilter (refer related doc).
    Allowed filters:
    - by organism owner of the object => created_by (owner id)
    """

    owner_id = filters.NumberFilter(field_name="owner")

    class Meta:
        model = Segment
        fields = {"owner_id": ["exact"]}


class VisitFilter(BaseModelFilter):
    """Filter for Visit instances:

    Herits from BaseModelFilter (refer related doc).
    Allowed filters:
    - by organism owner of the object => created_by (owner id)
    """

    # is_pole = filters.DateFilter(field_name="pole", lookup_expr="pole__isnull")
    # is_segment = filters.DateFilter(field_name="segment", lookup_expr="segment__isnull")
    visit_date = filters.DateFilter(
        field_name="visit_date", lookup_expr="date"
    )
    from_visit_date = filters.DateFilter(
        field_name="visit_date", lookup_expr="date__gte"
    )
    to_visit_date = filters.DateFilter(
        field_name="visit_date", lookup_expr="date__lte"
    )

    class Meta:
        model = Visit
        fields = [
            "visit_date",
            "from_visit_date",
            "to_visit_date",
        ]


class EquipmentFilter(filters.FilterSet):
    """Filter for both types of Equipment instances (Pole & Segment)

    If no value given for "pole" (and/or "segment") parameter (get parameters), no filter will be applied to Poles (and/or Segment) all instances will be returned with result"""

    class Meta:
        model = Operation
        fields = ["installed"]


class PoleEquipmentFilter(filters.FilterSet):
    """Filter for Pole Equipment instances"""

    class Meta:
        model = Operation
        fields = ["pole", "installed"]


class SegmentEquipmentFilter(filters.FilterSet):
    """Filter for Segment Equipment instances"""

    class Meta:
        model = Operation
        fields = ["segment", "installed"]
