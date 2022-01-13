#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import gettext_lazy as _
from sinp_nomenclatures.models import Item as Nomenclature

from commons.models import BaseModel
from media.models import Picture


class Mortality(BaseModel):
    """Mortality model extending BaseModel model with metadata fields

    Describe a mortality case.
    """

    species = models.ForeignKey(
        Nomenclature,
        on_delete=models.PROTECT,
        limit_choices_to={"type__mnemonic": "species"},
        null=True,
        blank=True,
        related_name="species_name",
        verbose_name=_("Species"),
        help_text=_("Species"),
    )
    nb_death = models.IntegerField(_("Number found dead"), default=1)
    death_cause = models.ForeignKey(
        Nomenclature,
        on_delete=models.PROTECT,
        limit_choices_to={"type__mnemonic": "cause_of_death"},
        null=True,
        blank=True,
        related_name="+",
        verbose_name=_("Cause of death"),
        help_text=_("Cause of death"),
    )
    data_source = models.ForeignKey(
        Nomenclature,
        on_delete=models.PROTECT,
        limit_choices_to={"type__mnemonic": "death_data_source"},
        null=True,
        blank=True,
        related_name="mortality_data_source",
        verbose_name=_("Mortality data source"),
        help_text=_("Mortality data source"),
    )
    pictures = models.ManyToManyField(
        Picture,
        blank=True,
        related_name="mortality_pictures",
        verbose_name=_("Picture related to the mortality case"),
        help_text=_("Picture related to the mortality case"),
    )

    def __str__(self):
        return f"Moratlity Case :{self.species} - {self.created_by} - {self.timestamp_create:%d-%m-%Y %H:%M}"
