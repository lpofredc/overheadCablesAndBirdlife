#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import datetime
from uuid import uuid4

from django.contrib.gis.db import models as gis_models
from django.db import models
from django.utils.translation import gettext_lazy as _
from sinp_nomenclatures.models import Item as Nomenclature

from commons.models import BaseModel
from geo_area.models import GeoArea
from media.models import Picture
from sensitive_area.models import SensitiveArea


class Infrastructure(BaseModel):
    """Common shared infrastructure model with metadata fields

    Abstract class: all specific infrastructure classes will inherit from this class.

    uuid is a unique identifier (not primary key). It can be used as data identifier in case of
    data gathered from various origin (e.g. populating data from various DB)
    """

    uuid = models.UUIDField(
        default=uuid4,
        unique=True,
        editable=False,
        verbose_name=_("Identifiant unique"),
    )

    class Meta:
        abstract = True


class Pole(Infrastructure):
    """Pole model extending infrastructure model with metadata fields

    Define an electric pole.
    """

    geom = gis_models.PointField(null=True, blank=True, srid=4326)
    geo_area = models.ManyToManyField(
        GeoArea,
        blank=True,
        db_table="pole_geo_areas",
        related_name="pole_geo_area",
        verbose_name=_("Associated Administrative and Natural Areas"),
        help_text=_("Associated Administrative and Natural Areas"),
    )
    sensitivity_areas = models.ManyToManyField(
        SensitiveArea,
        blank=True,
        db_table="pole_sensitive_areas",
        related_name="pole_sensitive_area",
        verbose_name=_("Associated Sensitivity Areas"),
        help_text=_("Associated Sensitivity Areas"),
    )


class Segment(Infrastructure):
    """Segment model extending infrastructure model with metadata fields

    Define a power line segment.
    """

    geom = gis_models.LineStringField(null=True, blank=True, srid=4326)
    geo_area = models.ManyToManyField(
        GeoArea,
        blank=True,
        db_table="sgmt_geo_areas",
        related_name="sgmt_geo_area",
        verbose_name=_("Associated Administrative and Natural Areas"),
        help_text=_("Associated Administrative and Natural Areas"),
    )
    sensitive_areas = models.ManyToManyField(
        SensitiveArea,
        blank=True,
        db_table="sgmt_sensitive_areas",
        related_name="sgmt_sensitive_area",
        verbose_name=_("Associated Sensitivity Areas"),
        help_text=_("Associated Sensitivity Areas"),
    )


class Observation(BaseModel):
    """Observation model with metadata fields

    Observation instance contains information related to an infrastructure (pole or segment).
    Planned use: one instance of Observation is created to record initial infrastructure information. Then, new instances may be created for information update. Previous existing intances assure trailing of infrastructure related data.

    uuid is a unique identifier (not primary key). It can be used as data identifier in case of
    data gathered from various origin (e.g. populating data from various DB)
    """

    uuid = models.UUIDField(
        default=uuid4,
        unique=True,
        editable=False,
        verbose_name=_("unique Id"),
    )
    pole = models.ForeignKey(
        Pole,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        editable=False,
        related_name="observation_pole",
        verbose_name=_("Pole attached with this observation"),
        help_text=_("Pole attached with this observation"),
    )
    segment = models.ForeignKey(
        Segment,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        editable=False,
        related_name="observation_segment",
        verbose_name=_("Segment attached with this observation"),
        help_text=_("Segment attached with this observation"),
    )
    inventory_date = models.DateTimeField(
        _("Inventory date"), editable=False, default=datetime.now()
    )
    observation_date = models.DateTimeField(
        _("Observation date"), default=datetime.now()
    )
    observation = models.TextField(_("Observation"), blank=True, null=True)
    neutralized = models.BooleanField(_("Neutralized"), default=False)
    pictures = models.ManyToManyField(
        Picture,
        related_name="observation_pictures",
        verbose_name=_("Segment attached with this observation"),
        help_text=_("Segment attached with this observation"),
    )
    condition = models.ForeignKey(
        Nomenclature,
        on_delete=models.PROTECT,
        limit_choices_to={"type__mnemonic": "infrastr_condition"},
        null=True,
        blank=True,
        editable=False,
        related_name="pole_condition",
        verbose_name=_("Pole condition"),
        help_text=_("Pole condition"),
    )
    isolation_advice = models.BooleanField(
        _("Isolation"),
        null=True,
        blank=True,
    )
    dissuasion_advice = models.BooleanField(
        _("Dissuasion"),
        null=True,
        blank=True,
    )
    attraction_advice = models.BooleanField(
        _("Attraction"),
        null=True,
        blank=True,
    )
    pole_type_primary = models.ForeignKey(
        Nomenclature,
        on_delete=models.PROTECT,
        limit_choices_to={"type__mnemonic": "pole_type"},
        null=True,
        related_name="pole_type_primary",
        verbose_name=_("Primary pole type"),
        help_text=_("Primary pole type"),
    )
    pole_type_secondary = models.ForeignKey(
        Nomenclature,
        on_delete=models.PROTECT,
        limit_choices_to={"type__mnemonic": "pole_type"},
        null=True,
        related_name="pole_type_secondary",
        verbose_name=_("Secondary pole type"),
        help_text=_("Secondary pole type"),
    )
    pole_attractivity = models.ForeignKey(
        Nomenclature,
        on_delete=models.PROTECT,
        limit_choices_to={"type__mnemonic": "risk_level"},
        null=True,
        related_name="pole_attractivity",
        verbose_name=_("Attractivity level of risk"),
        help_text=_("Attractivity level of risk"),
    )
    pole_dangerousness = models.ForeignKey(
        Nomenclature,
        on_delete=models.PROTECT,
        limit_choices_to={"type__mnemonic": "risk_level"},
        null=True,
        related_name="pole_dangerousness",
        verbose_name=_("dangerousness level of risk"),
        help_text=_("dangerousness level of risk"),
    )
    segt_build_integr_risk = models.ForeignKey(
        Nomenclature,
        on_delete=models.PROTECT,
        limit_choices_to={"type__mnemonic": "risk_level"},
        related_name="segment_building_integration_risk",
        verbose_name=_("Building integration level of risk"),
        help_text=_("Building integration level of risk"),
    )
    segt_moving_risk = models.ForeignKey(
        Nomenclature,
        on_delete=models.PROTECT,
        limit_choices_to={"type__mnemonic": "risk_level"},
        related_name="segment_moving_risk",
        verbose_name=_("moving level of risk"),
        help_text=_("moving level of risk"),
    )
    sgmt_topo_integr_risk = models.ForeignKey(
        Nomenclature,
        on_delete=models.PROTECT,
        limit_choices_to={"type__mnemonic": "risk_level"},
        related_name="segment_topological_integration_risk",
        verbose_name=_("topological level of risk"),
        help_text=_("Topological level of risk"),
    )
    sgmt_veget_integr_risk = models.ForeignKey(
        Nomenclature,
        on_delete=models.PROTECT,
        limit_choices_to={"type__mnemonic": "risk_level"},
        related_name="segment_vegetation_risk",
        verbose_name=_("vegetation level of risk"),
        help_text=_("vegetation level of risk"),
    )

    class Meta:
        constraints = [
            models.CheckConstraint(
                name="%(app_label)s_%(class)s_only_one_of_both_field_not_null_constraint",
                check=(
                    models.Q(
                        pole__isnull=False,
                        segment__isnull=True,
                    )
                    | models.Q(
                        pole__isnull=True,
                        segment__isnull=False,
                    )
                ),
            )
        ]


class Equipment(BaseModel):
    """Equipment model with metadata fields

    Equipment instance contains information related to an equipment installed on an infrastructure (pole or segment).
    Planned use: one instance of Equipment is created to record equipment installation. Each installed equipment matches to an Equipment instance.

    uuid is a unique identifier (not primary key). It can be used as data identifier in case of
    data gathered from various origin (e.g. populating data from various DB)
    """

    uuid = models.UUIDField(
        default=uuid4,
        unique=True,
        editable=False,
        verbose_name=_("unique Id"),
    )
    pole = models.ForeignKey(
        Pole,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        editable=False,
        related_name="equipment_pole",
        verbose_name=_("Pole the equipment is installed on"),
        help_text=_("Pole the equipment is installed on"),
    )
    segment = models.ForeignKey(
        Segment,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        editable=False,
        related_name="equipment_segment",
        verbose_name=_("Segment the equipment is installed on"),
        help_text=_("Segment the equipment is installed on"),
    )
    equipment_date = models.DateTimeField(
        editable=False, default=datetime.now()
    )
    pictures = models.ManyToManyField(
        Picture,
        related_name="equipment_pictures",
        verbose_name=_("Segment attached with this observation"),
        help_text=_("Segment attached with this observation"),
    )
    installed = models.BooleanField(
        _("Installed"),
        null=True,
        blank=True,
    )
    pole_eqmt_type = models.ForeignKey(
        Nomenclature,
        on_delete=models.PROTECT,
        limit_choices_to={"type__mnemonic": "pole_equipment"},
        related_name="equipment_pole_eqmt_type",
        verbose_name=_("Type of equipment for pole"),
        help_text=_("Type of equipment for pole"),
    )
    sgmt_eqmt_type = models.ForeignKey(
        Nomenclature,
        on_delete=models.PROTECT,
        limit_choices_to={"type__mnemonic": "pole_equipment"},
        related_name="equipment_sgmt_eqmt_type",
        verbose_name=_("Type of equipment for segment"),
        help_text=_("Type of equipment for segment"),
    )
    pole_nb_equipments = models.IntegerField(
        _("Number of equipments"), null=True, blank=True
    )

    class Meta:
        constraints = [
            models.CheckConstraint(
                name="%(app_label)s_%(class)s_only_one_of_both_field_not_null_constraint",
                check=(
                    models.Q(
                        pole__isnull=False,
                        segment__isnull=True,
                    )
                    | models.Q(
                        pole__isnull=True,
                        segment__isnull=False,
                    )
                ),
            )
        ]
