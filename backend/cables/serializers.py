import logging

from rest_framework.exceptions import APIException
from rest_framework_gis.serializers import (
    GeoFeatureModelSerializer,
    ModelSerializer,
)
from rest_polymorphic.serializers import PolymorphicSerializer
from sinp_nomenclatures.serializers import (
    NomenclatureSerializer as NomenclatureSerializer,
)

from geo_area.models import GeoArea
from geo_area.serializers import GeoAreaSerializer
from media.serializers import MediaSerializer
from sensitive_area.models import SensitiveArea
from sensitive_area.serializers import SensitiveAreaSerializer

from .models import Action, Diagnosis, Infrastructure, Line, Operation, Point


class ActionSerializer(ModelSerializer):
    """Serializer for Action

    Used to serialize all data from actions.
    """

    media = MediaSerializer(many=True)

    class Meta:
        model = Action
        fields = ["id", "infrastructure", "date", "remark", "media"]


class DiagnosisSerializer(ModelSerializer):
    """Serializer for Diagnosis

    Used to serialize all data from Diagnosis.
    """

    # Allow to display nested data
    condition = NomenclatureSerializer(read_only=True)
    pole_type = NomenclatureSerializer(many=True, read_only=True)
    pole_attractivity = NomenclatureSerializer(read_only=True)
    pole_dangerousness = NomenclatureSerializer(read_only=True)
    sgmt_build_integr_risk = NomenclatureSerializer(read_only=True)
    sgmt_moving_risk = NomenclatureSerializer(read_only=True)
    sgmt_topo_integr_risk = NomenclatureSerializer(read_only=True)
    sgmt_veget_integr_risk = NomenclatureSerializer(read_only=True)
    media = MediaSerializer(many=True, read_only=True)

    class Meta:
        model = Diagnosis
        fields = [
            "id",
            "infrastructure",
            "date",
            "remark",
            "neutralized",
            "condition",
            "condition_id",
            "isolation_advice",
            "dissuasion_advice",
            "attraction_advice",
            "pole_type",
            "pole_type_id",
            "pole_attractivity",
            "pole_attractivity_id",
            "pole_dangerousness",
            "pole_dangerousness_id",
            "sgmt_build_integr_risk",
            "sgmt_build_integr_risk_id",
            "sgmt_moving_risk",
            "sgmt_moving_risk_id",
            "sgmt_topo_integr_risk",
            "sgmt_topo_integr_risk_id",
            "sgmt_veget_integr_risk",
            "sgmt_veget_integr_risk_id",
            "media",
            "media_id",
            "last",
        ]
        # Allow to handle create/update/partial_update with nested data
        extra_kwargs = {
            "condition_id": {"source": "condition", "write_only": True},
            "pole_type_id": {"source": "pole_type", "write_only": True},
            "pole_attractivity_id": {
                "source": "pole_attractivity",
                "write_only": True,
            },
            "pole_dangerousness_id": {
                "source": "pole_dangerousness",
                "write_only": True,
            },
            "sgmt_build_integr_risk_id": {
                "source": "sgmt_build_integr_risk",
                "write_only": True,
            },
            "sgmt_moving_risk_id": {
                "source": "sgmt_moving_risk",
                "write_only": True,
            },
            "sgmt_topo_integr_risk_id": {
                "source": "sgmt_topo_integr_risk",
                "write_only": True,
            },
            "sgmt_veget_integr_risk_id": {
                "source": "sgmt_veget_integr_risk",
                "write_only": True,
            },
            "media_id": {"source": "media", "write_only": True},
        }

        """Overriden create method for Diagnosis

        This method was overidden to implement a customized behaviour specific to application structure.
        New Diagnosis related to an Infrastructure (Point or Line) is created with field "last=True". That means it is current state of diagnosis for the Infrastructure.
        In case of new Diagnosis on same Infrastructure, the new one is created with "last=True" as current one. Older ones (should be exactly 1) then become "last=False" due to this method.
        APIException is raised if there is not exactly 1 Diagnosis with "last=True". If issue occures with attachment of ManyToMany fields data, Diagnostic is deleted (if it was created) and an APIException is raised.
        """

    def create(self, validated_data):
        old_diags = Diagnosis.objects.all().filter(
            infrastructure=validated_data["infrastructure"]
        )
        for diag in old_diags:
            diag.last = False
            diag.save()
        # gather data for ManyToMany fields (and removing related data from validated_data)
        poleType_data = validated_data.pop("pole_type")
        media_data = validated_data.pop("media")
        # create Diagnosis

        newDiag = Diagnosis.objects.create(**validated_data)

        checkLast = Diagnosis.objects.all().filter(
            infrastructure=validated_data["infrastructure"], last=True
        )
        if len(checkLast) != 1:
            msg = "Diagnosis traceability issue"
            logging.error(msg)
            raise APIException(msg)

        try:
            # set data to ManyToMany fields od newDiag
            newDiag.pole_type.set(poleType_data)
            newDiag.media.set(media_data)

        except Exception:
            if newDiag is not None:
                newDiag.delete()
            msg = "Issue with Diagnosis configuration. No Diagnosis created."
            logging.error(msg)
            raise APIException(msg)

        return newDiag  # return new Diagnostic


class OperationSerializer(ModelSerializer):
    """Serializer for Operation

    Used to serialize all data from operations.
    """

    # Allow to display nested data
    operation_type = NomenclatureSerializer(read_only=True)
    eqmt_type = NomenclatureSerializer(read_only=True)
    media = MediaSerializer(many=True, read_only=True)

    class Meta:
        model = Operation
        fields = [
            "id",
            "infrastructure",
            "date",
            "remark",
            "operation_type",
            "operation_type_id",
            "eqmt_type",
            "eqmt_type_id",
            "media",
            "media_id",
        ]
        # Allow to handle create/update/partial_update with nested data
        extra_kwargs = {
            "operation_type_id": {
                "source": "operation_type",
                "write_only": True,
            },
            "eqmt_type_id": {"source": "eqmt_type", "write_only": True},
            "media_id": {"source": "media", "write_only": True},
        }

        """Overriden create method for Operation

        This method was overidden to implement a customized behaviour specific to application structure.
        New Operation related to an Infrastructure (Point or Line) is created with field "last=True". That means it is current state of operations for the Infrastructure.
        In case of new Operation on same Infrastructure, the new one is created with "last=True" as current one. Older ones (should be only 1) then become "last=False" due to this method.
        Exception is raised if there is not exactly 1 Operation with "last=True"
        """

    # def create(self, validated_data):
    #     old_ops = Operation.objects.all().filter(infrastructure=validated_data["infrastructure"])
    #     for op in old_ops:
    #         op.last = False
    #         op.save()

    #     # check there is exactly 1 'CURRENT' Operation for the Infrastructure
    #     current = Operation.objects.all().filter(
    #         infrastructure=validated_data["infrastructure"], last=True
    #     )
    #     if len(current) != 1:
    #         logging.error("Operation traceability issue")
    #         raise APIException("Operation traceability issue")

    #     return Operation.objects.create(**validated_data)


class InfrastructureSerializer(GeoFeatureModelSerializer):
    """Serializer for Infrastructure

    Used to serialize all data from infrastructures.
    inherit from GeoAreaSerializer as contains geo data.
    """

    # Allow to display nested data
    owner = NomenclatureSerializer()
    geo_area = GeoAreaSerializer(many=True)
    sensitive_area = SensitiveAreaSerializer(many=True)
    actions_infrastructure = ActionSerializer(many=True)

    class Meta:
        model = Infrastructure
        geo_field = "geom"
        fields = [
            "id",
            "owner",
            "geom",
            "geo_area",
            "sensitive_area",
            "actions_infrastructure",
        ]


class ActionPolymorphicSerializer(PolymorphicSerializer):
    """Serializer for Action taking into account polymorphismrequest"""

    model_serializer_mapping = {
        Action: ActionSerializer,
        Diagnosis: DiagnosisSerializer,
        Operation: OperationSerializer,
    }


class PointSerializer(GeoFeatureModelSerializer):
    """Serializer for Point

    Used to serialize all data from Point.
    inherit from GeoAreaSerializer as contains geo data.
    """

    # Allow to display nested data
    owner = NomenclatureSerializer(read_only=True)
    geo_area = GeoAreaSerializer(many=True, read_only=True)
    sensitive_area = SensitiveAreaSerializer(many=True, read_only=True)
    actions_infrastructure = ActionPolymorphicSerializer(
        many=True, read_only=True
    )

    class Meta:
        model = Point
        geo_field = "geom"
        fields = [
            "id",
            "geom",
            "owner",
            "owner_id",
            "geo_area",
            # "geo_area_id",
            "sensitive_area",
            # "sensitive_area_id",
            "actions_infrastructure",
        ]
        # Allow to handle create/update/partial_update with nested data
        extra_kwargs = {
            "owner_id": {"source": "owner", "write_only": True},
            # "geo_area_id": {"source": "geo_area", "write_only": True},
            # "sensitive_area_id": {"source": "sensitive_area", "write_only": True},
        }

        """ Overidden method to create Point

        At Point creation, method search all GeoArea and all SensitiveArea that contain new Point coordinates, and set GeoArea id list to Point field geo_area (Infrastructure.geo_area) and SensitiveArea id list to Point field sensitive_area (Infrastructure.sensitive_area).
        If issue occures for attachment with sensitive/geo areas, the Point is deleted (if it was created) and an APIException is raised.
        """

    def create(self, validated_data):
        # create Point object with given coordinates
        point = Point.objects.create(**validated_data)

        try:
            # get lists of GeoArea and Sensitive_Area containing Point location
            geoareas = GeoArea.objects.all().filter(
                geom__intersects=point.geom
            )
            sensitiveareas = SensitiveArea.objects.all().filter(
                geom__intersects=point.geom
            )
            # set the lists to point.geo_area and save it
            point.geo_area.set(geoareas)
            point.sensitive_area.set(sensitiveareas)
            point.save()

        except Exception:
            if point is not None:
                point.delete()
            msg = "Issue with attachment from new point to sensitive/geo areas. No Point created."
            logging.error(msg)
            raise APIException(msg)

        return point


class LineSerializer(GeoFeatureModelSerializer):
    """Serializer for Line

    Used to serialize all data from lines.
    inherit from GeoAreaSerializer as contains geo data.
    """

    # Allow to display nested data
    owner = NomenclatureSerializer(read_only=True)
    geo_area = GeoAreaSerializer(many=True, read_only=True)
    sensitive_area = SensitiveAreaSerializer(many=True, read_only=True)
    actions_infrastructure = ActionSerializer(many=True, read_only=True)

    class Meta:
        model = Line
        geo_field = "geom"
        fields = [
            "id",
            "geom",
            "owner",
            "owner_id",
            "geo_area",
            # "geo_area_id",
            "sensitive_area",
            # "sensitive_area_id",
            "actions_infrastructure",
        ]
        # Allow to handle create/update/partial_updcreateate with nested data
        extra_kwargs = {
            "owner_id": {"source": "owner", "write_only": True},
            # "geo_area_id": {"source": "geo_area", "write_only": True},
            # "sensitive_area_id": {"source": "sensitive_area", "write_only": True},
        }


class InfrastructurePolymorphicSerializer(
    PolymorphicSerializer, GeoFeatureModelSerializer
):
    """Serializer for Infrastructure taking into account polymorphism

    Used to serialize all data from infrastructures.
    This allow handle specific data for classe inheriting from InfrastructureModel (e.g. Pole, Segment), as each object from inheriting classes are instances of InfrastructureModel.
    Inherit from PolymorphicSerializer.
    """

    model_serializer_mapping = {
        Infrastructure: InfrastructureSerializer,
        Point: PointSerializer,
        Line: LineSerializer,
    }

    class Meta:
        model = Infrastructure
        geo_field = "geom"
