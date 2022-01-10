from django.db import models
from django.utils.translation import gettext_lazy as _
from sinp_nomenclatures.models import Item as Nomenclature

from .basemodel import BaseModel


class MortalityCase(BaseModel):
    """MortalityCase model extending BaseModel model with metadata fields

    Describe a mortality case.
    """

    species = models.ForeignKey(
        "Species", verbose_name=_("+"), on_delete=models.DO_NOTHING
    )
    death_cause = models.ForeignKey(
        Nomenclature,
        on_delete=models.DO_NOTHING,
        limit_choices_to={"type__mnemonic": "death_cause"},
        null=True,
        blank=True,
        related_name="+",
        verbose_name=_("Cause of death"),
        help_text=_("Cause of death"),
    )

    class Meta:
        app_label = "cables"
