# from uuid import uuid4

from django.contrib.gis.db import models as gis_models
from django.db import models
from django.utils.translation import gettext_lazy as _
from sinp_nomenclatures.models import Item as Nomenclature

from .basemodel import BaseModel


class Infrastructure(BaseModel):
    """Common shared infrastructure model with metadata fields

    Abstract class: all specific infrastructure classes will inherit from this class
    """

    # uuid = models.UUIDField(
    #     default=uuid4,
    #     unique=True,
    #     editable=False,
    #     verbose_name=_("Identifiant unique"),
    # )
    geom = gis_models.PointField(null=True, blank=True, srid=4326)
    remark = models.TextField(_("Remark"), blank=True, null=True)
    neutralized = models.BooleanField(_("Neutralized"), default=False)
    pole_condition = models.ForeignKey(
        Nomenclature,
        null=True,
        blank=True,
        editable=False,
        related_name="+",
        on_delete=models.DO_NOTHING,
    )
    sensitivity_areas = models.ForeignKey(
        "SensitiveArea",
        verbose_name=_("Related sensitive area"),
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    class Meta:
        app_label = "cables"
        abstract = True


class Pole(Infrastructure):
    """Pole model extending infrastructure model with metadata fields

    Describe an electric pole.
    """

    isolation_advice = models.BooleanField(_("Isolation"), default=False)
    dissuasion_advice = models.BooleanField(_("Dissuasion"), default=False)
    attraction_advice = models.BooleanField(_("Attraction"), default=False)
    pole_type_primary = models.ForeignKey(
        Nomenclature,
        on_delete=models.DO_NOTHING,
        limit_choices_to={"type__mnemonic": "pole_type"},
        null=True,
        related_name="+",
        verbose_name=_("Pole type"),
        help_text=_("Pole type"),
    )
    pole_type_secondary = models.ForeignKey(
        Nomenclature,
        on_delete=models.DO_NOTHING,
        limit_choices_to={"type__mnemonic": "pole_type"},
        null=True,
        related_name="+",
        verbose_name=_("Pole type"),
        help_text=_("Pole type"),
    )
    pole_attractivity = models.ForeignKey(
        Nomenclature,
        on_delete=models.DO_NOTHING,
        limit_choices_to={"type__mnemonic": "risk_level"},
        null=True,
        related_name="+",
        verbose_name=_("Level of risk"),
        help_text=_("Level of risk"),
    )
    pole_dangerousness = models.ForeignKey(
        Nomenclature,
        on_delete=models.DO_NOTHING,
        limit_choices_to={"type__mnemonic": "risk_level"},
        null=True,
        related_name="+",
        verbose_name=_("Level of risk"),
        help_text=_("Level of risk"),
    )

    class Meta:
        app_label = "cables"


class Segment(Infrastructure):
    """Segment model extending infrastructure model with metadata fields

    Describe a power line segment.
    """

    building_integration_risk = models.ForeignKey(
        Nomenclature,
        on_delete=models.DO_NOTHING,
        limit_choices_to={"type__mnemonic": "risk_level"},
        related_name="+",
        verbose_name=_("Level of risk"),
        help_text=_("Level of risk"),
    )
    moving_risk = models.ForeignKey(
        Nomenclature,
        on_delete=models.DO_NOTHING,
        limit_choices_to={"type__mnemonic": "risk_level"},
        related_name="+",
        verbose_name=_("Level of risk"),
        help_text=_("Level of risk"),
    )
    topological_integration_risk = models.ForeignKey(
        Nomenclature,
        on_delete=models.DO_NOTHING,
        limit_choices_to={"type__mnemonic": "risk_level"},
        related_name="+",
        verbose_name=_("Level of risk"),
        help_text=_("Level of risk"),
    )
    vegetation_integration_risk = models.ForeignKey(
        Nomenclature,
        on_delete=models.DO_NOTHING,
        limit_choices_to={"type__mnemonic": "risk_level"},
        related_name="+",
        verbose_name=_("Level of risk"),
        help_text=_("Level of risk"),
    )

    class Meta:
        app_label = "cables"
