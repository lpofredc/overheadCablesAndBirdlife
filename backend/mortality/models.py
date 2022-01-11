from django.db import models
from django.utils.translation import gettext_lazy as _
from sinp_nomenclatures.models import Item as Nomenclature

from trackable_basemodel.models import BaseModel


# TODO temporary species allowing creation of MortalityCase Model, awaiting this be defined
class Species(models.Model):
    name = models.CharField(_("Species Name"), max_length=50)


class Meta:
    app_label = "mortality"


class Case(BaseModel):
    """Case model extending BaseModel model with metadata fields

    Describe a mortality case.
    """

    species = models.ForeignKey(
        "Species",
        verbose_name=_("+"),
        null=True,
        blank=True,
        on_delete=models.DO_NOTHING,
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
        app_label = "mortality"
