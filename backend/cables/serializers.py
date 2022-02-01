from rest_framework_gis.serializers import (
    GeoFeatureModelSerializer,
    ModelSerializer,
)
from rest_polymorphic.serializers import PolymorphicSerializer
from sinp_nomenclatures.serializers import ItemSerializer

from geo_area.serializers import GeoAreaSerializer
from media.serializers import MediaSerializer
from sensitive_area.serializers import SensitiveAreaSerializer

from .models import Action, Infrastructure, Operation, Pole, Segment, Visit


class ActionSerializer(ModelSerializer):
    """Serializer for Action

    Used to serialize all data from actions.
    """

    media = MediaSerializer(many=True)

    class Meta:
        model = Action
        exclude = ["uuid"]


class VisitSerializer(ActionSerializer):
    """Serializer for Visit

    Used to serialize all data from visits.
    """

    condition = ItemSerializer()
    pole_type = ItemSerializer()
    pole_attractivity = ItemSerializer()
    pole_dangerousness = ItemSerializer()
    sgmt_build_integr_risk = ItemSerializer()
    sgmt_moving_risk = ItemSerializer()
    sgmt_topo_integr_risk = ItemSerializer()
    sgmt_veget_integr_risk = ItemSerializer()

    class Meta:
        model = Visit
        fields = [
            "infrastructure",
            "date",
            "remark",
            "neutralized",
            "condition",
            "isolation_advice",
            "dissuasion_advice",
            "attraction_advice",
            "pole_type",
            "pole_attractivity",
            "pole_dangerousness",
            "sgmt_build_integr_risk",
            "sgmt_moving_risk",
            "sgmt_topo_integr_risk",
            "sgmt_veget_integr_risk",
            "media",
        ]


class OperationSerializer(ActionSerializer):
    """Serializer for Operation

    Used to serialize all data from operations.
    """

    operation_type = ItemSerializer()
    eqmt_type = ItemSerializer()

    class Meta:
        model = Visit
        fields = [
            "infrastructure",
            "date",
            "remark",
            "operation_type",
            "eqmt_type",
            "media",
        ]


class InfrastructureSerializer(GeoAreaSerializer):
    """Serializer for Infrastructure

    Used to serialize all data from infrastructures.
    inherit from GeoAreaSerializer as contains geo data.
    """

    owner = ItemSerializer()
    geo_area = GeoAreaSerializer(many=True)
    sensitive_area = SensitiveAreaSerializer(many=True)
    actions_infrastructure = ActionSerializer(many=True)

    class Meta:
        model = Infrastructure
        geo_field = "geom"
        fields = [
            "id",
            "owner",
            "geo_area",
            "sensitive_area",
            "actions_infrastructure",
        ]


class ActionPolymorphicSerializer(PolymorphicSerializer):
    """Serializer for Action taking into account polymorphism

    Used to serialize all data from actions.
    This allow handle specific data for classe inheriting from ActionModel (e.g. Visit, Operation), as each object from inheriting classes are instances of ActionModel.
    Inherit from PolymorphicSerializer.
    """

    model_serializer_mapping = {
        Action: ActionSerializer,
        Visit: VisitSerializer,
        Operation: OperationSerializer,
    }


class PoleSerializer(GeoFeatureModelSerializer):
    """Serializer for Pole

    Used to serialize all data from poles.
    inherit from GeoAreaSerializer as contains geo data.
    """

    owner = ItemSerializer()
    geo_area = GeoAreaSerializer(many=True)
    sensitive_area = SensitiveAreaSerializer(many=True)
    actions_infrastructure = ActionPolymorphicSerializer(many=True)

    class Meta:
        model = Pole
        geo_field = "geom"
        fields = [
            "id",
            "geom",
            "owner",
            "geo_area",
            "sensitive_area",
            "actions_infrastructure",
        ]


class PoleWriteSerializer(GeoFeatureModelSerializer):
    """Serializer for Pole: used for creation and updating

    Used to serialize all data from poles.
    inherit from GeoAreaSerializer as contains geo data.
    """

    class Meta:
        model = Pole
        geo_field = "geom"
        fields = [
            "geom",
            "owner",
            "geo_area",
            "sensitive_area",
            "actions_infrastructure",
        ]


class SegmentSerializer(GeoFeatureModelSerializer):
    """Serializer for Segment

    Used to serialize all data from segments.
    inherit from GeoAreaSerializer as contains geo data.
    """

    owner = ItemSerializer()
    geo_area = GeoAreaSerializer(many=True)
    sensitive_area = SensitiveAreaSerializer(many=True)
    actions_infrastructure = ActionSerializer(many=True)

    class Meta:
        model = Segment
        geo_field = "geom"
        fields = [
            "id",
            "geom",
            "owner",
            "geo_area",
            "sensitive_area",
            "actions_infrastructure",
        ]


class SegmentWriteSerializer(GeoFeatureModelSerializer):
    """Serializer for Segment: used for creation and updating

    Used to serialize all data from segments.
    inherit from GeoAreaSerializer as contains geo data.
    """

    class Meta:
        model = Segment
        geo_field = "geom"
        fields = [
            "id",
            "geom",
            "owner",
            "geo_area",
            "sensitive_area",
            "actions_infrastructure",
        ]

    # def update(self, instance, validated_data):
    #     #     for op in validated_data["operation_pole"]:
    #     #         op = Operation(pole=instance)
    #     #         op.save()

    #     op = Operation(pole=instance)

    #     op.save()

    #     return instance


class InfrastructurePolymorphicSerializer(PolymorphicSerializer):
    """Serializer for Infrastructure taking into account polymorphism

    Used to serialize all data from infrastructures.
    This allow handle specific data for classe inheriting from InfrastructureModel (e.g. Pole, Segment), as each object from inheriting classes are instances of InfrastructureModel.
    Inherit from PolymorphicSerializer.
    """

    model_serializer_mapping = {
        Infrastructure: InfrastructureSerializer,
        Pole: PoleSerializer,
        Segment: SegmentSerializer,
    }

    # def update(self, instance, validated_data):
    #     #     for op in validated_data["operation_pole"]:
    #     #         op = Operation(pole=instance)
    #     #         op.save()

    #     op = Operation(pole=instance)

    #     op.save()

    #     return instance


# class ElemSerializer(ModelSerializer):
#     class Meta:
#         model = Elem
#         fields = ["desc"]


# class PotoSerializer(ModelSerializer):
#     elem = ElemSerializer(many=True)

#     class Meta:
#         model = Poto
#         fields = ["id", "elem"]

#     def update(self, instance, validated_data):
#         for item in validated_data["elem"]:
#             elem = Elem(desc=item["desc"], poto=instance)
#             elem.save()

#         return instance


# #################################################################################################
# class InfrastructureSerializer(ModelSerializer):
#     """Serializer for Pole model

#     Allow to get all data from poles (including nested) but not allow create and update"""

#     owner = ItemSerializer()
#     geo_area = GeoAreaSerializer(many=True)
#     sensitive_area = SensitiveAreaSerializer(many=True)

#     class Meta:
#         model = Infrastructure
#         fields = ["id", "owner", "geo_area", "sensitive_area"]


class PoleSerializerInfo(GeoFeatureModelSerializer):
    """Serializer for Pole model

    Allow to get all data from poles (including nested) but not allow create and update"""

    owner = ItemSerializer()
    geo_area = GeoAreaSerializer(many=True)
    sensitive_area = SensitiveAreaSerializer(many=True)

    class Meta:
        model = Pole
        geo_field = "geom"
        fields = ["id", "geom", "owner", "geo_area", "sensitive_area"]


class PoleSerializerEdit(GeoFeatureModelSerializer):
    """Serializer for Pole model

    Allow to get data from poles (not nested data, only FK) but allow create and update"""

    class Meta:
        model = Pole

        geo_field = "geom"
        fields = ["id", "geom", "owner", "geo_area", "sensitive_area"]


class SegmentSerializerInfo(ModelSerializer):
    """Serializer for Segment model

    Allow to get all data from segments (including nested) but not allow create and update"""

    owner = ItemSerializer()
    geo_area = GeoAreaSerializer(many=True)
    sensitive_area = SensitiveAreaSerializer(many=True)

    class Meta:
        model = Segment
        fields = ["id", "geom", "owner", "geo_area", "sensitive_area"]


class SegmentSerializerEdit(ModelSerializer):
    """Serializer for Segment model

    Allow to get data from segments (not nested data, only FK) but allow create and update"""

    class Meta:
        model = Segment
        fields = ["id", "geom", "owner", "geo_area", "sensitive_area"]


class VisitSerializerInfo(ModelSerializer):
    """Serializer for Visit model

    Allow to get all data from visits (including nested) but not allow create and update"""

    pole = PoleSerializerInfo()
    segment = SegmentSerializerInfo()
    media = MediaSerializer(many=True)
    condition = ItemSerializer()
    pole_type = ItemSerializer()
    pole_attractivity = ItemSerializer()
    pole_dangerousness = ItemSerializer()
    sgmt_build_integr_risk = ItemSerializer()
    sgmt_moving_risk = ItemSerializer()
    sgmt_topo_integr_risk = ItemSerializer()
    sgmt_veget_integr_risk = ItemSerializer()

    class Meta:
        model = Visit
        exclude = ["uuid"]


class VisitSerializerEdit(ModelSerializer):
    """Serializer for Visit model

    Allow to get data from visits (not nested data, only FK) but allow create and update"""

    class Meta:
        model = Visit
        exclude = ["uuid"]


class OperationSerializerInfo(ModelSerializer):
    """Serializer for Operation model

    Allow to get all data from operations (including nested) but not allow create and update"""

    # pole = PoleSerializerInfo()
    segment = SegmentSerializerInfo()
    media = MediaSerializer(many=True)
    eqmt_type = ItemSerializer()

    class Meta:
        model = Operation
        exclude = ["uuid"]


class OperationSerializerEdit(ModelSerializer):
    """Serializer for Operation model

    Allow to get data from operations (not nested data, only FK) but allow create and update"""

    class Meta:
        model = Operation
        exclude = ["uuid"]
