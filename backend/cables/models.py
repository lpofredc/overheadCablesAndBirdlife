#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from uuid import uuid4

from django.contrib.gis.db import models as gis_models
from django.db import models
from django.utils.translation import gettext_lazy as _
from sinp_nomenclatures.models import Item as Nomenclature

from commons.models import BaseModel
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
    infrastr_id = models.CharField(
        _("Infrastructure Id"),
        max_length=50,
        default="",
        unique=True,
    )
    remark = models.TextField(_("Remark"), blank=True, null=True)
    neutralized = models.BooleanField(_("Neutralized"), default=False)
    sensitivity_areas = models.ForeignKey(
        SensitiveArea,
        verbose_name=_("Related sensitive area"),
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    class Meta:
        abstract = True


class Pole(Infrastructure):
    """Pole model extending infrastructure model with metadata fields

    Describe an electric pole.
    """

    geom = gis_models.PointField(null=True, blank=True, srid=4326)
    isolation_advice = models.BooleanField(_("Isolation"), default=False)
    dissuasion_advice = models.BooleanField(_("Dissuasion"), default=False)
    attraction_advice = models.BooleanField(_("Attraction"), default=False)
    type_primary = models.ForeignKey(
        Nomenclature,
        on_delete=models.PROTECT,
        limit_choices_to={"type__mnemonic": "pole_type"},
        null=True,
        related_name="pole_type_primary",
        verbose_name=_("Primary pole type"),
        help_text=_("Primary pole type"),
    )
    type_secondary = models.ForeignKey(
        Nomenclature,
        on_delete=models.PROTECT,
        limit_choices_to={"type__mnemonic": "pole_type"},
        null=True,
        related_name="pole_type_secondary",
        verbose_name=_("Secondary pole type"),
        help_text=_("Secondary pole type"),
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
    attractivity = models.ForeignKey(
        Nomenclature,
        on_delete=models.PROTECT,
        limit_choices_to={"type__mnemonic": "risk_level"},
        null=True,
        related_name="pole_attractivity",
        verbose_name=_("Attractivity level of risk"),
        help_text=_("Attractivity level of risk"),
    )
    dangerousness = models.ForeignKey(
        Nomenclature,
        on_delete=models.PROTECT,
        limit_choices_to={"type__mnemonic": "risk_level"},
        null=True,
        related_name="pole_dangerousness",
        verbose_name=_("dangerousness level of risk"),
        help_text=_("dangerousness level of risk"),
    )


class Segment(Infrastructure):
    """Segment model extending infrastructure model with metadata fields

    Describe a power line segment.
    """

    geom = gis_models.LineStringField(null=True, blank=True, srid=4326)
    building_integration_risk = models.ForeignKey(
        Nomenclature,
        on_delete=models.PROTECT,
        limit_choices_to={"type__mnemonic": "risk_level"},
        related_name="segment_building_integration_risk",
        verbose_name=_("Building integration level of risk"),
        help_text=_("Building integration level of risk"),
    )
    moving_risk = models.ForeignKey(
        Nomenclature,
        on_delete=models.PROTECT,
        limit_choices_to={"type__mnemonic": "risk_level"},
        related_name="segment_moving_risk",
        verbose_name=_("moving level of risk"),
        help_text=_("moving level of risk"),
    )
    topological_integration_risk = models.ForeignKey(
        Nomenclature,
        on_delete=models.PROTECT,
        limit_choices_to={"type__mnemonic": "risk_level"},
        related_name="segment_topological_integration_risk",
        verbose_name=_("topological level of risk"),
        help_text=_("Topological level of risk"),
    )
    vegetation_integration_risk = models.ForeignKey(
        Nomenclature,
        on_delete=models.PROTECT,
        limit_choices_to={"type__mnemonic": "risk_level"},
        related_name="segment_vegetation_risk",
        verbose_name=_("vegetation level of risk"),
        help_text=_("vegetation level of risk"),
    )


class Visit(BaseModel):
    """Common shared Visit model with metadata fields

    Abstract class: all specific Visit classes will inherit from this class.

    uuid is a unique identifier (not primary key). It can be used as data identifier in case of
    data gathered from various origin (e.g. populating data from various DB)
    """

    # TODO content to be reviwed

    uuid = models.UUIDField(
        default=uuid4,
        unique=True,
        editable=False,
        verbose_name=_("Identifiant unique"),
    )
    observation = models.TextField(_("Observation"), blank=True, null=True)

    class Meta:
        abstract = True


class PoleVisit(Visit):
    """Pole Visit model with metadata fields

    PoleVisit class describes a visit for a pole infrastructure.
    Can be a simple observation visit or operation with equipment added.
    Observation and pictures can be added in both cases.
    In case of equipment installation, equipment field is added.
    """

    # TODO content to be defined
    observation = models.TextField(_("Observation"), blank=True, null=True)
    infrastructure = models.ForeignKey(
        Pole,
        on_delete=models.CASCADE,
        related_name="pole_dangerousness",
        verbose_name=_("Related infrastructure"),
        help_text=_("Related infrastructure"),
    )


class SegmentVisit(Visit):
    """Pole Visit model with metadata fields

    PoleVisit class describes a visit for a pole infrastructure.
    Can be a simple observation visit or operation with equipment added.
    Observation and media can be added in both cases.
    In case of equipment installation, equipment field is added.
    """

    # TODO content to be defined
    observation = models.TextField(_("Observation"), blank=True, null=True)
    infrastructure = models.ForeignKey(
        Segment,
        on_delete=models.CASCADE,
        related_name="pole_dangerousness",
        verbose_name=_("Related infrastructure"),
        help_text=_("Related infrastructure"),
    )
