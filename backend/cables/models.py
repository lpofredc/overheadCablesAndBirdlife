#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from uuid import uuid4

from django.contrib.gis.db import models as gis_models
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from sinp_nomenclatures.models import Item as Nomenclature

from commons.models import BaseModel
from geo_area.models import GeoArea
from media.models import Media
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
    owner = models.ForeignKey(
        Nomenclature,
        on_delete=models.PROTECT,
        limit_choices_to={"type__mnemonic": "organism"},
        null=True,
        blank=True,
        related_name="%(class)s_owner",
        verbose_name=_("Infrastructure owner organism"),
        help_text=_("Infrastructure owner organism"),
    )
    geo_area = models.ManyToManyField(
        GeoArea,
        blank=True,
        related_name="%(class)s_geo_area",
        verbose_name=_("Associated Administrative and Natural Areas"),
        help_text=_("Associated Administrative and Natural Areas"),
    )
    sensitivity_area = models.ManyToManyField(
        SensitiveArea,
        blank=True,
        related_name="%(class)s_sensitive_area",
        verbose_name=_("Associated Sensitivity Areas"),
        help_text=_("Associated Sensitivity Areas"),
    )

    class Meta:
        abstract = True


class Pole(Infrastructure):
    """Pole model extending infrastructure model with metadata fields

    Define an electric pole.
    """

    geom = gis_models.PointField(null=True, blank=True, srid=4326)

    def __str__(self):
        return f"Pole-({self.id})"


class Segment(Infrastructure):
    """Segment model extending infrastructure model with metadata fields

    Define a power line segment.
    """

    geom = gis_models.LineStringField(null=True, blank=True, srid=4326)

    def __str__(self):
        return f"Segment-({self.id})"


class Visit(BaseModel):
    """Visit model with metadata fields

    Visit instance contains information related to an infrastructure (pole or segment).
    Planned use: one instance of Visit is created to record initial infrastructure information. Then, new instances may be created for information update. Previous existing intances assure trailing of infrastructure related data.

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
        related_name="visit_pole",
        verbose_name=_("Pole attached with this visit"),
        help_text=_("Pole attached with this visit"),
    )
    segment = models.ForeignKey(
        Segment,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name=_("Segment attached with this visit"),
        help_text=_("Segment attached with this visit"),
    )
    visit_date = models.DateField(_("Visit date"), default=timezone.now)
    visit = models.TextField(_("Visit"), blank=True, null=True)
    neutralized = models.BooleanField(_("Neutralized"), default=False)
    media = models.ManyToManyField(
        Media,
        blank=True,
        related_name="visit_media",
        verbose_name=_("Media attached with this visit"),
        help_text=_("Media attached with this visit"),
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

    def __str__(self):
        return (
            f"Visit for Pole {self.id}"
            if (self.segment__isnull)
            else f"Visit for Segment {self.id}"
        )


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
        related_name="equipment_pole",
        verbose_name=_("Pole the equipment is installed on"),
        help_text=_("Pole the equipment is installed on"),
    )
    segment = models.ForeignKey(
        Segment,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="equipment_segment",
        verbose_name=_("Segment the equipment is installed on"),
        help_text=_("Segment the equipment is installed on"),
    )
    # equipment_date = models.DateTimeField(
    #     editable=False, default=datetime.now()
    # )
    media = models.ManyToManyField(
        Media,
        blank=True,
        related_name="equipment_media",
        verbose_name=_("Media attached with this equipment"),
        help_text=_("Media attached with this equipment"),
    )
    installed = models.BooleanField(
        _("Installed"),
        null=True,
        blank=True,
    )
    eqmt_type = models.ForeignKey(
        Nomenclature,
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        limit_choices_to={"type__mnemonic": "equipment_type"},
        related_name="equipment_pole_eqmt_type",
        verbose_name=_("Type of equipment for pole"),
        help_text=_("Type of equipment for pole"),
    )
    pole_nb_equipments = models.PositiveIntegerField(
        _("Number of equipments"), default=1
    )

    class Meta:
        constraints = [
            models.CheckConstraint(
                name="%(app_label)s_%(class)s_only_one_infrastructure_constraint",
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
            ),
        ]

    def __str__(self):
        return (
            f"Equipment for Pole {self.id} (Type: {self.eqmt_type})"
            if (self.pole)
            else f"Equipment for Segment {self.id} (Type: {self.eqmt_type})"
        )
